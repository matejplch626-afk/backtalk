# Czech translation status

This file is the continuity anchor for the Czech localization of BackTalk.

## Repositories and branches

- Upstream project: `trypsynth/backtalk`
- Upstream branch: `master`
- Czech fork: `matejplch626-afk/backtalk`
- Working branch: `czech-translation`
- Last upstream commit checked: `5e2fae60d1c2ed3f057db938ee9b46268a82daf4` (`Let each braille keyboard vibration be turned off on its own (#89)`, 2026-10-07)

## Localization strategy

BackTalk inherits a large existing Czech translation from Google's TalkBack. Do not translate TalkBack from scratch.

For BackTalk-specific strings:

1. Add new Czech resources under the corresponding `values-cs` directory.
2. Prefer separate feature-specific files when the resource key is new.
3. Do not duplicate an existing Czech resource name in a supplementary file.
4. If BackTalk changes the meaning of an existing TalkBack resource key, edit the inherited Czech resource value in its original Czech file instead of creating a duplicate.
5. Preserve Android format placeholders, plurals, XML escaping, XLIFF markup, and `translatable="false"` semantics exactly.
6. Do not localize internal preference keys or other `donottranslate` data.
7. Validate resources with an actual Gradle/AAPT build before considering the localization complete.

## Czech files added or extended for BackTalk

### Main TalkBack app

Under `talkback/src/main/res/values-cs/`:

- `strings_backtalk.xml` — low-latency audio, automatic language/dialect switching, screen announcements, lift-to-activate, wrap-around navigation, rotor gestures, proximity speakerphone behavior, audio routing, TTS options, long-text sentence mode, incoming notifications
- `strings_control_sounds.xml` — control sounds/vibrations, 3D audio, control sound labels
- `strings_sound_themes.xml` — sound themes, install/remove/export, custom sounds/vibrations, Braille keyboard sounds
- `strings_direct_touch.xml` — Direct touch and app-specific direct typing
- `strings_on_device_ai.xml` — on-device AI model UI/errors
- `strings_pause.xml` — pause/resume BackTalk
- `strings_radial_menu.xml` — circle/radial menu
- `strings_update.xml` — built-in updater
- `strings_gemini_api_key.xml` — Gemini API key settings
- `strings_gemini_errors.xml` — Gemini API/quota errors
- `strings_individual_feedback.xml` — individual sounds/vibrations, including six independently switchable Braille keyboard vibrations added upstream in #89

### Braille IME

Under `braille/brailleime/src/phone/res/values-cs/`, `strings_backtalk.xml` covers orientation announcements/settings, Braille keyboard typing sounds/echo, vertical dot swap, and skip tutorial.

### Braille common

Under `braille/common/src/phone/res/values-cs/`, `strings_backtalk.xml` covers the orientation-lock gesture label.

## Important commits in the Czech branch

- `276effcbb6825c13dc222706c2d4a74a5c7fd37f` — initial BackTalk-specific Czech strings
- `885c622875751031eb4cd52e5233da6779a22eb9` — initial Braille orientation additions
- `9104fa801add12524d7fa98ed998c6afb19c17e3` — lift activation, wrap-around, rotor gestures, call routing
- `b823d08891ff36c71329a69ff89b70f2639a2aae` — speech and notification settings
- `69d6f06647f92ad8ccfadfcb9eb67ed808809d88` — corrected Czech validation workflow; successful audit/build run followed
- `169a66615d7cc65de4b11c3db6605d35043769b8` — Czech labels for six new Braille keyboard vibration controls from upstream #89

## Upstream watch log

### 2026-10-07 — through `5e2fae60d1c2ed3f057db938ee9b46268a82daf4`

Upstream advanced by 13 commits from the previous checkpoint `f4cdc0d3f46f4f6a946824ee7b24c236c6487f1e`. Most changes were code, CI, dependencies, documentation, TV behavior, or non-translatable resources. Commit #89 added six new user-visible English string resources for independently controlling Braille keyboard vibrations. Czech translations were added for all six. No placeholders, XLIFF markup, or plurals are involved in these six strings.

New Czech labels:

- Braille keyboard: typing a character → `Braillská klávesnice: zadání znaku`
- space or delete → `Braillská klávesnice: mezera nebo mazání`
- new line or deleting a word → `Braillská klávesnice: nový řádek nebo smazání slova`
- holding fingers down → `Braillská klávesnice: přidržení prstů`
- other gestures → `Braillská klávesnice: ostatní gesta`
- nothing to delete → `Braillská klávesnice: není co smazat`

## Completed BackTalk-specific areas

The Czech branch includes translations for sound themes, control sounds/vibrations, 3D audio, custom sounds, screen/tabletop orientation, audio routing, rotor behavior, lift-to-activate, wrap-around navigation, proximity speakerphone behavior, Direct touch, on-device AI, Gemini settings/errors, Pause BackTalk, circle menu, updater, Braille keyboard additions, TTS options, sentence-at-a-time mode, incoming notifications, and individual Braille keyboard vibration controls.

## Audit and build status

GitHub Actions workflow `Czech translation audit and build` completed successfully in run #7 on 2026-10-06. It audited changed existing English keys, applied Czech semantic updates, checked duplicate Czech resource names, validated XML and simple-string placeholders, completed the Gradle debug build, and produced phone/Wear APK artifacts.

The audit also identified broad inherited branding changes from `TalkBack` to `Backtalk`; remaining branding-only and semantic changes should be reviewed before the initial upstream Czech PR.

## Test APK status

A successful test artifact was produced from run #7: `backtalk-phone-debug.apk` plus a Wear build. BackTalk application ID is `fyi.quin.backtalk`, so it is expected to install alongside system/Google TalkBack as a separate accessibility service. Published debug builds use a debug signing key.

Runtime test sequence: install the phone APK, keep system TalkBack enabled initially, confirm BackTalk appears separately in Android accessibility settings, then begin controlled Czech localization testing.

## Remaining work before declaring 100% coverage

1. Finish review of remaining changed existing keys, especially inherited `TalkBack` → `Backtalk` branding and semantic changes.
2. Runtime-test Czech strings on a real Android device.
3. Correct terminology, truncation, missing strings, malformed announcements, or feature-specific issues found in testing.
4. Re-run validation/build after final corrections and after syncing current upstream code.
5. Prepare the initial professional upstream PR to `trypsynth/backtalk:master`.

## Maintenance workflow

For every new upstream commit/release: compare from the recorded checkpoint; inspect English translatable resources in TalkBack/Braille; translate new keys; audit changed existing keys; preserve placeholders/XLIFF/plurals; commit focused Czech changes; update this checkpoint; validate/build when the branch contains the corresponding upstream code; and submit small upstream PRs once coherent and tested.

## Upstream contribution policy

Prefer small, reviewable pull requests rather than a permanently open mega-PR. After upstream accepts the initial Czech localization, subsequent BackTalk features should normally be delivered as focused Czech translation updates tied to relevant upstream changes.

## Initial professional upstream PR plan

Do not open the first upstream PR until the Czech localization has passed real-device testing and remaining audit findings have been reviewed. The PR should explain that BackTalk inherits Google's Czech TalkBack localization; this contribution adds/updates BackTalk-specific Czech strings; inherited Czech strings change only where English meaning/branding changed; Android formatting semantics were preserved; resources passed automated validation/build; and localization was tested by a native Czech daily screen-reader user.

Matěj Plch is willing to act as the Czech localization maintainer/contact. Upstream developers need not translate Czech themselves; focused Czech follow-up PRs can be submitted when English user-facing strings change.

Suggested wording:

> Czech localization is maintained continuously. I am a native Czech speaker and daily screen reader user. I can keep Backtalk-specific Czech strings updated as new features are added. You don't need to maintain the Czech translations yourself; I will submit small follow-up pull requests whenever English user-facing strings change.
