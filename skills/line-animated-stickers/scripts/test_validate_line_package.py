"""Small synthetic fixtures: no user art or external service is modified."""
import io
import struct
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

from PIL import Image, ImageDraw

from validate_line_package import validate_package, validate_png


def png(size, seed, animated=True, loop=2, duration=200, dpi=(72, 72)):
    frames = []
    for i in range(5 if animated else 1):
        frame = Image.new("RGBA", size)
        ImageDraw.Draw(frame).rectangle((8, 8, size[0] - 9, size[1] - 9),
                                        fill=(seed, 40 + 30 * i, 100, 255))
        frames.append(frame)
    output = io.BytesIO()
    frames[0].save(output, format="PNG", save_all=animated, append_images=frames[1:],
                   duration=duration, loop=loop, disposal=0, blend=0, dpi=dpi)
    return output.getvalue()


class PackageTests(unittest.TestCase):
    def check_package(self, changes=None, count=8, sticker_type="animated"):
        animated = sticker_type == "animated"
        size = (280, 270) if animated else (370, 320)
        files = {f"{i:02}.png": png(size, 10 + i, animated) for i in range(1, count + 1)}
        files.update({"main.png": png((240, 240), 100, animated), "tab.png": png((96, 74), 110, False)})
        files.update(changes or {})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "upload.zip"
            with ZipFile(path, "w") as archive:
                for name, data in files.items():
                    archive.writestr(name, data)
            return validate_package(path, sticker_type)

    def test_supported_counts(self):
        for count in (8, 16, 24):
            with self.subTest(count=count):
                result = self.check_package(count=count)
                self.assertTrue(result["passed"])
                self.assertEqual(result["animated_stickers"], count)

    def test_rejects_static_sticker(self):
        with self.assertRaisesRegex(ValueError, "APNG"):
            self.check_package({"01.png": png((280, 270), 11, False)})

    def test_rejects_infinite_plays(self):
        with self.assertRaisesRegex(ValueError, "finite plays"):
            self.check_package({"01.png": png((280, 270), 11, loop=0)})

    def test_rejects_fractional_total(self):
        with self.assertRaisesRegex(ValueError, "total playback"):
            self.check_package({"01.png": png((280, 270), 11, duration=150)})

    def test_rejects_over_four_seconds(self):
        with self.assertRaisesRegex(ValueError, "total playback"):
            self.check_package({"01.png": png((280, 270), 11, loop=4, duration=400)})

    def test_rejects_bad_png_crc(self):
        data = bytearray(png((280, 270), 11))
        data[-1] ^= 1
        with self.assertRaisesRegex(ValueError, "PNG CRC"):
            self.check_package({"01.png": bytes(data)})

    def test_rejects_extra_files(self):
        with self.assertRaisesRegex(ValueError, "Requires 8, 16, 24"):
            self.check_package({"preview.html": b"not an upload image"})

    def test_rejects_duplicate_stickers(self):
        with self.assertRaisesRegex(ValueError, "Duplicate sticker files"):
            self.check_package({"02.png": png((280, 270), 11)})

    def test_static_supported_counts_and_small_canvas(self):
        for count in (8, 16, 24, 32, 40):
            with self.subTest(count=count):
                result = self.check_package({"01.png": png((100, 100), 11, False)}, count, "static")
                self.assertTrue(result["passed"])
                self.assertEqual(result["static_stickers"], count)
                self.assertEqual(result["animated_main"], 0)

    def test_static_rejects_wrong_encoding_and_dimensions(self):
        for data, error in [
            (png((280, 270), 11), "static PNG without animation"),
            (png((371, 320), 11, False), "canvas outside bounds"),
            (png((369, 318), 11, False), "dimensions must be even"),
            (png((370, 320), 11, False, dpi=(36, 36)), "72dpi"),
        ]:
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                self.check_package({"01.png": data}, sticker_type="static")

    def test_static_main_and_tab_dimensions(self):
        for name in ("main.png", "tab.png"):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, "requires"):
                self.check_package({name: png((100, 100), 100, False)}, sticker_type="static")

    def test_animation_rejects_static_only_count(self):
        with self.assertRaisesRegex(ValueError, "Requires 8, 16, 24"):
            self.check_package(count=32)

    def test_rejects_excessive_frame_header_before_decoding(self):
        data = bytearray(png((280, 270), 11))
        position = data.index(b"acTL")
        struct.pack_into(">I", data, position + 4, 1_000_000)
        struct.pack_into(">I", data, position + 12, zlib.crc32(data[position:position + 12]) & 0xffffffff)
        with patch("validate_line_package.Image.open", side_effect=AssertionError("Unexpected decoder call")):
            with self.assertRaisesRegex(ValueError, "before decoding"):
                validate_png("01.png", bytes(data))


if __name__ == "__main__":
    unittest.main()
