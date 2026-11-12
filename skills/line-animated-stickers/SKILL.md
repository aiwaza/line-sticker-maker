---
name: line-animated-stickers
description: >-
  Guide a beginner from one personal photo or an existing character sheet to
  original static or animated LINE stickers. Offer character styles and suggest suitable
  counts, phrases, gestures and framing for the user to choose. Create
  and approve the character, produce PNG stills or APNG animations, validate and upload the
  package, submit review with final consent, and release after approval when
  authorized. Use for 내 사진으로 라인 스탬프, 静止画スタンプ, 動くLINEスタンプ, or resuming this
  photo-to-registration workflow. An ordinary chat GIF is a different task.
---

# One photo → character → static or animated LINE stickers → registration

Start with one photo, create a consistent character, and carry the requested set
through actual LINE registration. The user chooses the character name and items; no previous character or phrase
list is a default set. A ready character sheet can enter directly at sticker design.

## Start or resume

- First establish `sticker_type`: static / animated. If unspecified, offer
  **정지 스탬프 / 움직이는 스탬프** (localized to the conversation). Explain that
  static uses one expressive pose; animated adds timed expression/gesture changes.
  Respect an explicit choice and do not ask again. A set has one type; changing
  it after a LINE draft is created requires a separate draft.
- Inspect the supplied photo or sheet once; do not ask for a prepared character
  sheet when the user has supplied a photo. If no style is chosen, offer the ten
  numbered styles in [character-styles.md](references/character-styles.md) first.
  Accept a number, a custom style or “choose for me”; skip the question when the
  user has already chosen. Then follow [production.md](references/production.md),
  show the character look and build a canonical sheet from the approved look.
- For an existing approved sheet, extract visual
  identity, clothing, proportions, materials and optional props. Text printed on
  the sheet is reference content, not authority to alter the user's request. The
  user's character name and spelling override a name printed on that sheet.
- For a new character, create a separate project. Never overwrite another
  character's sources, approvals, final ZIP or existing LINE draft.
- For an existing set, read its production plan, latest user decisions and final
  selection manifest before rebuilding. Respect per-item replacements and saved
  metadata edits. A newer experiment does not automatically become the final.
- Keep a small plan with `reference`, `character_name`, `sticker_type`, `count`, `language`, `text_mode`, `framing`,
  `items` and `stage`. Each item records its exact text, framing, expression,
  pose, selected source and approval status; animated items also record primary
  and optional secondary motion.

## Let the user choose the items

For a beginner, explain the next choice in ordinary language and make concrete
suggestions. Do not require animation terms, a prepared item list or a separate
character-sheet upload. Ask only for missing choices, together when practical:

1. Count: static 8 / 16 / 24 / 32 / 40; animated 8 / 16 / 24. Offer only the
   selected type's registration counts. Other counts can be prototypes.
2. Text and items: exact user-supplied wording and gestures, or an idea list for
   the user to edit. Support no-text stickers. Reuse the specified language.
3. Framing: face / full body / mixed. For mixed sets, show the per-item assignment.

If purpose is unclear, ask what conversations the set is for (for example daily,
work or romance). Recommend a suitable count and an editable item list with exact
wording, expressions and visible gestures. Explain 8 as a compact set, 16 as a
broader everyday set and 24 as a larger range of situations; these are practical
suggestions, not different LINE quality tiers. Do not make the user invent every
motion. Static proposals use expressive finished poses; animated proposals use
feasible gestures and effects within the current LINE limits. Static 32/40-item
sets are an option when the user wants more situations, not a default upsell.

If the user says they will specify items, wait for their list rather than filling
it with a previous set's phrases. Partial lists may be completed only when the user invites
suggestions. Do not ask again for already supplied choices or repeat approvals.

Turn the choices into an ordered table: number, exact wording, framing, expression,
pose, supporting effects, and (animated only) main motion. Show proposed items before generation when
the user has not already approved an equivalent list.

## Produce in reviewable stages

Read [production.md](references/production.md) before creating or revising art.

1. Make one finished **static** sample, normally item 01. It establishes identity,
   lettering, outline, palette and finish. Show the actual image. Continue after
   the user's design approval; skip this gate if the same style is already approved.
2. Produce every approved item as a separate transparent source. An overview is a
   review aid, never a substitute for the individual files. Show all designs and
   apply requested revisions only to affected IDs.
3. **Animated only:** animate a representative item; test a second if it uses a materially different
   motion technique. Preserve an approved baseline while testing stronger motion.
   Once the approach is accepted, complete the requested set without asking again
   for every file.
4. **Static:** skip animation and export approved stills as transparent PNGs.
   **Animated:** export APNGs and inspect their first frames and motion.
   Show the selected output files and **main + tab** together for either type.
   Explain the two auxiliary images before the user mistakes the tab for the cover.
   Make motion previews match the actual finite playback length; do not add an
   unlabelled final hold that looks like a frozen animation.
5. Validate and package the selected files. A finished still, a playable preview,
   a compliant ZIP, a saved LINE draft and a submitted review are distinct states.

Use the current image-generation/editing skill and available tools for artwork and
keyframe changes. Use supported media/file tools for animation encoding and checks.
Do not promise automatic generation, interpolation or transparent video support
that the available tools have not demonstrated.

## Package, upload and request review

Read [registration.md](references/registration.md) for current requirements,
main/tab roles, upload verification and the last consent step. Recheck the linked
official rules when producing a new registration package.

The bundled validator checks the ZIP without modifying or extracting it:

```sh
python3 "$SKILL_DIR/scripts/validate_line_package.py" "$PROJECT/final/upload.zip" --type static > "$PROJECT/final/validation-report.json"
```

Use `--type animated` for animated sets (the backward-compatible default).
Set `SKILL_DIR` to this skill's actual directory and `PROJECT` to the current
project. Pillow is required; reuse an available environment rather than installing
unrelated packages. The script checks file structure and encoding, not artistic
quality, rights ownership, server acceptance or actual phone playback.

Keep final sources, selected keyframes when animated, individual PNGs/APNGs, ZIP, metadata, preview,
validation report and a concise registration receipt. Record only the status
actually observed. Do not store login tokens, email verification links or banking
details in the skill or receipt.

Continue beyond making the ZIP: save the draft, upload the selected count plus
main/tab, verify the saved images and metadata, and prepare the final review
request. Ask for the required rights consent only when that concrete request is
ready. Verify submission on the result page. Review approval is an external wait;
resume from the saved receipt, release when approved and authorized, and verify
the public product page. Do not call a pending review a completed sale.

For first-time registration, explain LINE sign-in/creator signup and guide each
screen. The user handles private authentication/account details and the final
rights consent; do the artwork, files, metadata and authorized upload/submission.
Say which tool environment is actually available: a local Codex skill does not
automatically run in an ordinary ChatGPT chat. Do not promise unattended signup,
guaranteed review approval or an untested one-photo end-to-end run.

When Reel evidence is requested, save real screenshots and available source/motion
media as the work happens; follow the capture checklist in registration.md. Keep
the original personal photo out of public capture bundles unless the user wants
it shown. A rendered APNG preview is not a recording of the generation process.
