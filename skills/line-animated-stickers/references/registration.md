# LINE package and registration

## Official sources and measured limits

Static and animated dimensions, counts and timing rechecked 2026-11-12. Recheck before a new
package or price recommendation:

- [Static sticker guideline](https://creator.line.me/ja/guideline/sticker/)
- [Animated sticker guideline](https://creator.line.me/ja/guideline/animationsticker/)
- [Frame, timing and first-frame detail](https://creator.line.me/ja/guideline/animationsticker/detail/)
- [Official registration manual](https://linecreator-manual-ja.blog.jp/archives/5655078.html)
- [Review guideline](https://creator.line.me/ja/review_guideline/)

| Type | Sticker files | Sticker dimensions | Sticker / main / tab format |
|---|---|---|---|
| Static | 8, 16, 24, 32 or 40 | At most 370×320, even dimensions | PNG / PNG / PNG |
| Animated | 8, 16 or 24 | At most 320×270; width or height at least 270 | APNG / APNG / PNG |

For both types, main is 240×240 and tab is 96×74; file extension is `.png`.
Static exports require at least 72dpi; approximately 10px clear margins are the
official static guideline's recommendation. Do not impose animation's 270px
minimum dimension or frame/playback rules on static PNGs.

Use true transparency and RGB artwork. Each file must be at most 1MB and the ZIP
at most 60MB. This workflow uses conservative decimal limits of 1,000,000 and
60,000,000 bytes. For animated sets only, keep 5–20 frames and 1–4 finite plays. Cycle duration ×
plays must total 1, 2, 3 or 4 seconds, never exceed four seconds. `loop=0` means
infinite playback in APNG and is unsuitable. The first frame also serves as the
non-playing shop/chat image. Fully identical frames do not make a valid animation.

72dpi and approximately 6–8px clear animation margins were production
choices in an earlier animated set. Actual pixel size, safe movement and clean contours matter; do not present
those exact margins as universal platform requirements.

## Explain main and tab before upload

- **Main** is the representative image used to identify the product in the shop
  and product information. Choose an appealing, legible pose from the set, fit
  uniformly into a square and show it to the user with title and price.
- **Tab** is the small button for selecting the set while using stickers in chat.
  A large recognizable face can work better there than tiny full-body artwork.
  It is a different asset from the shop cover. Respect a requested alternative.
- LINE adds the animation/play indicator itself; do not paint it into either file.

Create a flat ZIP containing only `01.png` through the chosen count, `main.png`
and `tab.png`. Keep previews, source images, scripts, folders and macOS metadata
out of the upload archive. Run the validator with the selected `--type static`
or `--type animated`; inspect all stills or decoded first frames and motion.

## Metadata and account setup

Prepare English title/description (required) and requested language translations.
The limits are 40 for title, 50 for creator, 160 for description and 50 ASCII
characters for copyright. Full-width characters count as two; check the live
form counter. Avoid emoji/URLs in metadata and keep it consistent with the art.
Do not strip drawn hearts or decorations merely because metadata forbids emoji.

Reuse the public creator name/copyright already chosen for the same account.
Otherwise obtain the missing name rather than inventing a legal identity. Read
back the user's saved title; do not overwrite it from a stale packaging script.
Declare AI use accurately when the form asks. Review visibility, area, premium/
campaign participation, price and manual/automatic release settings.

Static and animated sets may have different available price tiers. Confirm the
live menu and compare actual LINE STORE products if the user asks about typical prices. App/region payment amounts can
differ from the displayed LINE STORE tier.

Let the user complete private sign-in and account information. A phone-opened
verification email can leave an older desktop link unhelpful; do not infer that
registration failed from that link alone. Open the official MyPage entry and
inspect the actual account state before asking for a new signup or repeated email.

If a deep link lands on a blank or stale login screen, try the known entry
`https://creator.line.me/my/` once, then use visible navigation. Keep the same selected
browser and follow its current automation documentation.

## Save the draft and upload

Use a suitable connector if available, otherwise the authorized browser. Select
**スタンプ** for static or **アニメーションスタンプ** for animated before saving.
Set the selected type's allowed count in the image editor before uploading.
The type cannot be changed afterward; create a separate draft if the user switches.
Confirm ordinary save/count dialogs within
the user's authorized task.

Use the documented file-chooser upload mechanism. Handle its wait rejection
immediately so a timeout cannot reset the automation session. Prefer semantic
locators and the actual file input where supported; if it fails, inspect fresh
state before the browser's documented alternative. Avoid stale numeric indices,
unverified scripts, hidden endpoints or bypassing denied OS controls.

Upload the exact verified ZIP. A timeout alone does not prove failure: inspect
whether processing has started or the slots have populated before uploading
again. Return from the editor to the saved draft and verify all N+2 slots, no
image errors, the selected replacement(s), and the saved count/metadata. Never
equate a chooser accepting a path with successful server storage.

On the tested form, loading placeholders briefly showed empty titles and the
wrong type/count. Wait for saved fields before editing. A label such as 保存 or
ZIPファイル アップロード can be the actual click target when an overlaid input
times out; inspect current state, then use the visible label rather than repeating
the same failed input click. Read back AI use after changing the sticker type.

Record draft ID/URL, uploaded ZIP hash, selected item hashes, count, observed
status and screenshot path. Do not record credentials, session/verification URLs,
bank branch, account number or account holder in the receipt or reusable skill.

## Payout, final consent and status

A notice that the payout destination is missing is an account setup issue. Open
**アカウント設定 → 送金先情報**, not **送金申請** (which requests transfer of
earnings). Let the user enter and save their banking details. Verify the save
notice or disappearance of the missing-destination notice without copying the
financial fields into logs/screenshots.

When the user authorizes submission, **リクエスト** opens the review confirmation.
It includes consent concerning copyright/portrait rights, necessary permissions,
and continued use by existing buyers after sales stop. Obtain the user's explicit
consent at that final step, or let them check **同意します** and press **OK**.
Explain the concrete LINE requirement instead of asking an unexplained repeat
permission. If they do it themselves, inspect the resulting state; do not submit
again.

Only report review submitted when the page says the request is complete and the
status changes, e.g. **審査待ち**. Save a result screenshot without private account
data. Approval, rejection and a live purchase URL are later states; do not invent
them or promise review timing. With manual release, sales require a separate
release action after approval. Do not call “uploaded” or “review waiting” a public
release, and do not create a monitoring automation unless requested.

After approval, perform the manual release when the user has authorized it.
Verify 販売中 and then the actual public LINE STORE page: correct title, creator,
price, own sticker gallery and purchase URL. If propagation is pending, preserve
the observed state and recheck; a temporary not-found page is not a live listing.
Do not purchase the product merely to test its page. If login, final consent or
external review blocks further work, save the exact stage and next action.

## Reel screenshots and media, when requested

Capture useful stages as they occur: approved character look and first still,
all-item overview, motion preview when animated, validated package, saved title/type/count, imported
images, price, final consent, submitted review, approval/release and public store.
Keep a chronological asset manifest with source, date, actual observed status and
whether each file is a screenshot, original artwork or an APNG-rendered video.

Save clean editorial copies without account headers, sign-in data or banking
fields. Keep raw reference captures separate from the shareable bundle. Include
only the creator's own gallery when a store page also shows other authors' work.
Label superseded, failed and propagation-pending screens; do not present them as
the completed result. Do not invent missing historical captures or call a rendered
animation a screen recording. Show the final result screenshot to the user. If
they want to see the browser, visibly open the correct character's draft rather
than leaving them on a different set's tab.
