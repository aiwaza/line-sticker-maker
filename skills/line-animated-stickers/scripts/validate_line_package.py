"""Read-only checks for transparent RGBA LINE static or animated sticker ZIPs."""
import argparse
import hashlib
import io
import json
import re
import struct
import sys
import zlib
from fractions import Fraction
from pathlib import Path
from zipfile import BadZipFile, ZipFile

from PIL import Image


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_png(name, data, sticker_type="animated"):
    require(sticker_type in ("static", "animated"), "Unknown sticker type")
    require(data[:8] == b"\x89PNG\r\n\x1a\n", f"{name}: not PNG")
    require(len(data) <= 1_000_000, f"{name}: exceeds 1MB")
    offset, controls, sequence, animation, size, kind = 8, [], [], None, None, b""
    while offset < len(data):
        require(offset + 12 <= len(data), f"{name}: truncated chunk")
        length = struct.unpack_from(">I", data, offset)[0]
        end = offset + 12 + length
        require(end <= len(data), f"{name}: truncated chunk payload")
        kind = data[offset + 4:offset + 8]
        content = data[offset + 8:end - 4]
        crc = struct.unpack_from(">I", data, end - 4)[0]
        require(zlib.crc32(kind + content) & 0xffffffff == crc, f"{name}: PNG CRC mismatch")
        if kind == b"IHDR":
            width, height, depth, color = struct.unpack_from(">IIBB", content)
            max_width, max_height = (370, 320) if sticker_type == "static" else (320, 270)
            require(0 < width <= max_width and 0 < height <= max_height, f"{name}: canvas outside bounds")
            if sticker_type == "static":
                require(width % 2 == 0 and height % 2 == 0, f"{name}: static dimensions must be even")
            # shortcut: RGBA sources only, widen if indexed PNG export is introduced.
            require(depth == 8 and color == 6, f"{name}: workflow requires 8-bit RGBA")
            size = (width, height)
        elif kind == b"acTL":
            animation = struct.unpack(">II", content)
        elif kind == b"fcTL":
            require(size is not None, f"{name}: missing canvas header")
            control = struct.unpack(">IIIIIHHBB", content)
            require(control[1] > 0 and control[2] > 0, f"{name}: empty frame")
            require(control[1] + control[3] <= size[0] and control[2] + control[4] <= size[1],
                    f"{name}: frame outside canvas")
            require(control[7] <= 2 and control[8] <= 1, f"{name}: invalid disposal/blend")
            controls.append(control)
            sequence.append(control[0])
        elif kind == b"fdAT":
            sequence.append(struct.unpack_from(">I", content)[0])
        offset = end
        if kind == b"IEND":
            require(length == 0, f"{name}: invalid end chunk")
            break
    require(offset == len(data) and kind == b"IEND", f"{name}: trailing data or missing end")
    require(sequence == list(range(len(sequence))), f"{name}: APNG sequence mismatch")
    if sticker_type == "static":
        require(animation is None and not controls, f"{name}: requires static PNG without animation")
    elif animation is not None:
        require(5 <= animation[0] <= 20 and animation[0] == len(controls),
                f"{name}: requires 5-20 complete APNG frames before decoding")
    with Image.open(io.BytesIO(data)) as image:
        frame_count, hashes, borders = image.n_frames, set(), []
        require(not image.info.get("default_image", False), f"{name}: include first frame in animation")
        for index in range(frame_count):
            image.seek(index)
            frame = image.convert("RGBA")
            require(frame.size == size, f"{name}: inconsistent frame canvas")
            alpha = frame.getchannel("A")
            require(alpha.getextrema() == (0, 255), f"{name}: missing transparent or opaque artwork")
            bounds = alpha.getbbox()
            borders.append(min(bounds[0], bounds[1], size[0] - bounds[2], size[1] - bounds[3]))
            hashes.add(hashlib.sha256(frame.tobytes()).hexdigest())
        dpi = image.info.get("dpi")
    duration, plays = Fraction(0), 0
    if sticker_type == "static":
        require(animation is None and not controls and frame_count == 1,
                f"{name}: requires static PNG without animation")
        require(dpi is not None and min(dpi) >= 72, f"{name}: static PNG requires at least 72dpi metadata")
        if name == "main.png":
            require(size == (240, 240), f"{name}: requires 240x240")
        elif name == "tab.png":
            require(size == (96, 74), f"{name}: requires static 96x74 PNG")
    elif name == "tab.png":
        require(size == (96, 74) and animation is None and frame_count == 1,
                f"{name}: requires static 96x74 PNG")
    else:
        require(animation is not None and animation[0] == frame_count == len(controls),
                f"{name}: requires complete APNG frames")
        require(5 <= frame_count <= 20 and len(hashes) >= 2, f"{name}: requires 5-20 changing frames")
        plays = animation[1]
        require(1 <= plays <= 4, f"{name}: requires 1-4 finite plays")
        duration = sum((Fraction(c[5] * 1000, c[6] or 100) for c in controls), Fraction(0))
        require(all(c[5] > 0 for c in controls), f"{name}: zero frame delay")
        require(duration * plays in (1000, 2000, 3000, 4000),
                f"{name}: total playback must be 1, 2, 3 or 4 seconds")
        if name == "main.png":
            require(size == (240, 240), f"{name}: requires 240x240")
        else:
            require(max(size) >= 270, f"{name}: one dimension must reach 270")
    return {"file": name, "size": list(size), "frames": frame_count,
            "unique_frames": len(hashes), "cycle_ms": float(duration), "plays": plays,
            "total_ms": float(duration * plays), "bytes": len(data), "dpi": dpi,
            "minimum_clear_border_px": min(borders), "png_crc": "passed",
            "sha256": hashlib.sha256(data).hexdigest()}


def validate_package(path, sticker_type="animated"):
    require(sticker_type in ("static", "animated"), "Unknown sticker type")
    path = Path(path)
    require(path.stat().st_size <= 60_000_000, "ZIP exceeds 60MB")
    with ZipFile(path) as archive:
        entries = archive.infolist()
        names = [entry.filename for entry in entries]
        require(len(names) == len(set(names)), "Duplicate ZIP member names")
        count = len(names) - 2
        allowed_counts = (8, 16, 24, 32, 40) if sticker_type == "static" else (8, 16, 24)
        require(count in allowed_counts, f"Requires {', '.join(map(str, allowed_counts))} stickers plus main/tab")
        expected = {f"{i:02}.png" for i in range(1, count + 1)} | {"main.png", "tab.png"}
        require(set(names) == expected, "ZIP must contain only flat numbered PNGs, main.png and tab.png")
        require(all(0 < e.file_size <= 1_000_000 for e in entries), "ZIP member exceeds 1MB or is empty")
        records = [validate_png(name, archive.read(name), sticker_type) for name in sorted(names)]
    sticker_hashes = [r["sha256"] for r in records if re.fullmatch(r"\d{2}\.png", r["file"])]
    require(len(set(sticker_hashes)) == count, "Duplicate sticker files in the set")
    return {"passed": True, "sticker_type": sticker_type, "sticker_count": count,
            "animated_stickers": count if sticker_type == "animated" else 0,
            "static_stickers": count if sticker_type == "static" else 0,
            "animated_main": int(sticker_type == "animated"), "static_main": int(sticker_type == "static"), "static_tab": 1,
            "zip": str(path.resolve()), "zip_bytes": path.stat().st_size,
            "zip_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "files": records,
            "policy": "Transparent 8-bit RGBA exports; pixel/encoding checks only",
            "not_checked": ["artistic quality", "lettering accuracy", "rights ownership",
                            "LINE server acceptance", "phone LINE playback"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip", type=Path)
    parser.add_argument("--type", choices=("static", "animated"), default="animated", dest="sticker_type")
    args = parser.parse_args()
    try:
        result = validate_package(args.zip, args.sticker_type)
    except (ValueError, OSError, BadZipFile, RuntimeError, struct.error) as error:
        print(json.dumps({"passed": False, "error": str(error)}, ensure_ascii=False, indent=2))
        sys.exit(1)
    print(json.dumps(result, ensure_ascii=False, indent=2))
