# Still and animated artwork production

## Start from one personal photo

Use the supplied photo to preserve visible facial features, hairstyle, hair color,
glasses and other requested details in a stylized character. Reuse the user's
chosen style; otherwise offer [the ten style choices](character-styles.md) and
help them choose. Do not
infer a person's occupation, name or personality from their appearance.

Show one character look for approval, then generate a compact canonical sheet
with a clear face and full-body pose. Record approved colors, clothing and
accessories. That sheet and the first accepted sticker become the references for
the remaining items; the user need not create or upload a separate sheet. An
already approved character sheet skips this step. Preserve the original photo as
a private project reference, outside the upload ZIP and public Reel bundle unless
the user specifically wants the photo included.

## Lock the new character's identity

Use the clearest complete pose in the supplied sheet as the identity reference.
Record hair silhouette/color, face proportions, eyes, skin, clothes, shoes,
accessories, head/body ratio and rendering material. Keep that source attached to
each generation; add the first approved sticker as a style reference afterward.
Do not transfer a previous character's lettering, face or material to a new
character unless requested.

For face stickers, include the complete head/hair, chin, neck and enough shoulders
for a natural silhouette; make hands visible when the gesture needs them. For full
body, keep the head, fingers, shoes and required props inside the canvas. A bath,
bed or seated scene may intentionally obscure the body; follow the user's scene.

## Still-image prompt pattern

Fill this pattern with the user's chosen item, not a preselected phrase:

```text
Create ONE independent finished messaging sticker, a STATIC design keyframe.
Reference 1 locks [character identity and clothing]. Reference 2, when present,
locks the approved sticker finish, outline and typography.
Keep [specific identity features], the same age impression and body proportions.
ITEM [id]: exact text “[verbatim wording]”; framing [face/full/scene].
Expression [specific]; pose [specific]; required props [specific].
Design character, lettering and small effects as one coherent composition.
Lettering must remain accurate and legible at the final sticker size, placed
around the character without hiding the face or becoming a subtitle banner.
Allow room for the intended motion. Keep the complete silhouette and wording
inside a landscape working canvas; preserve proportions rather than stretching.
True transparent alpha outside the artwork; no painted checkerboard, scenery,
watermark, numbering, or additional characters. Return one sticker, not a sheet.
```

Use generous generation margins to prevent initial clipping (a previous sample used
approximately 6% on each side), then fit the still's bounds (static) or the
*union of all frames* (animated) for the
final LINE canvas. That generation margin is a working choice, not an immutable
LINE whitespace requirement. Inspect readability at actual delivery size.

Store per-item source paths and prompts. Preserve a user's exact wording, including
long vowels and punctuation. Emoji may describe an effect rather than literal text;
clarify only if that distinction changes the design. Metadata text has different
character restrictions from lettering drawn into the sticker image.

## Export static stickers

For `sticker_type=static`, the approved stills are the final artwork: do not create
motion keyframes, GIFs or APNGs. Export transparent 8-bit RGBA PNGs within 370×320,
with even pixel dimensions and at least 72dpi. Preserve proportions and around
10px clear margins as recommended by the static guideline. Show all independent
PNGs with static 240×240 main and 96×74 tab. Check lettering, alpha edges and
complete silhouettes at delivery size, then package and validate with `--type static`.

The remaining motion/encoding sections apply only to animated sets.

## Animate the approved designs

Work from clean RGBA frames/keyframes. LINE's deliverable is APNG with a `.png`
extension; GIF is an optional sharing preview. Avoid a GIF-first conversion path
because GIF's palette and transparency can degrade an otherwise clean source.

Write a small timing plan per item: expression change, gesture, effect and return.
With a roughly two-second cycle, greeting hand motion, blinking and a small sun
rotation can coexist; a grateful expression and popping hearts can coexist.
Several simultaneous motions are allowed, but geometry and readability govern
whether a particular implementation is usable. Do not call a whole-image wobble
the requested hand wave or expression change.

Generate complete alternate poses when a limb or head changes substantially.
Keep shoulders/sleeves connected through every frame. A facial patch pasted over
static hair can leave a seam; animate a coherent head region instead. A rotated
isolated hand/arm can expose missing underlying art or cut a limb at its pivot.
For a doorway entrance, align complete scene cels to a stationary door jamb or
other scene anchor. Re-centering each changing silhouette makes the door drift.
An entrance may play once and stop; do not reverse the walk merely to force a loop.
Use explicit layers/masks rather than assuming a color means “text” or “hair” in
every character; dark text may overlap a dark jacket, for example.

When interpolating available keyframes, verify identity and color throughout.
Premultiplied-alpha processing helps avoid bright/dark fringe artifacts, but does
not repair inconsistent anatomy. Do not download/run an unverified model merely
because an old project mentions one. A renderer from another project may depend on its specific artwork.

For larger motion, keep the approved baseline and show one comparison. Look for:

- Hands, arms, shoes and lettering clipped during any part of the motion.
- Hair color flicker, stretched faces, extra limbs or fingers, detached shoulders.
- Head/hair seams, ghost text, background residue and damaged alpha edges.
- Jumping alignment between poses and a discontinuity when the cycle repeats.

If a stronger version fails, revise the affected item or keep the approved version
according to the user's choice. Preserve the exact per-item selection; do not replace unrelated files.

## Fit, encode and review

One working example used 10–16 frames, a 2-second cycle and 2 plays, total 4
seconds. Other valid timing choices are allowed. Changing the container does not
create missing frames or improve anatomical consistency.

Compute a common bounding box over the complete motion of each sticker. Fit
uniformly and use one stable canvas throughout that animation. This avoids both
large unnecessary margins and clipping at motion extremes. Different stickers may
have different dimensions within LINE limits; do not force every portrait into
an unnecessarily wide 320×270 canvas.

Keep the first frame expressive and complete: shops and non-playing views display
it as a still. Verify decoded frames, not just an encoder's success message. Show
actual APNGs with a replay control; finite playback can stop after four seconds.
Use a hash/version in preview image URLs after replacing an item to avoid stale
cached art. An MP4 contact sheet is useful for motion review, but is not an upload
asset. Check the final contours against both light and dark backgrounds.

Derive preview segment length from decoded frame durations multiplied by the
finite play count. A two-second single-play APNG should produce a two-second
faithful clip. If a separate inspection hold is useful, label it and keep it out
of the faithful preview. Re-encoding or renaming previews must not change the
approved APNGs or reset an existing registration receipt.

Freeze selection per ID with a SHA-256 before packaging. When replacing one item,
compare the old and new ZIP members so unrelated files, main and tab stay intact.
Keep experimental renderers from silently overwriting that final selection.
