# Czech translation status

This file is the continuity anchor for the Czech localization of BackTalk.

## Repositories and branches

- Upstream project: `trypsynth/backtalk`
- Upstream branch: `master`
- Czech fork: `matejplch626-afk/backtalk`
- Working branch: `czech-translation`
- Last upstream commit checked when this file was created: `f4cdc0d3f46f4f6a946824ee7b24c236c6487f1e` (`Grow the low-latency buffer when the fast mixer runs short (#71)`, 2026-10-06)

## Localization strategy

BackTalk inherits a large existing Czech translation from Google's TalkBack. Do not translate TalkBack from scratch.

For BackTalk-specific strings:

1. Add new Czech resources under the corresponding `values-cs` directory.
2. Prefer separate feature-specific files such as `strings_backtalk.xml`, `strings_sound_themes.xml`, etc. when the resource key is new.
3. Do not duplicate an existing Czech resource name in a supplementary file.
4. If BackTalk changes the meaning of an existing TalkBack resource key, edit the inherited Czech resource value in its original Czech file instead of creating a duplicate.
5. Preserve Android format placeholders, plurals, XML escaping, XLIFF markup, and `translatable="false"` semantics exactly.
6. Do not localize internal preference keys or other `donottranslate` data.
7. Validate resources with an actual Gradle/AAPT build before considering the localization complete.

## Czech files added or extended for BackTalk

### Main TalkBack app

Under `talkback/src/main/res/values-cs/`:

- `strings_backtalk.xml`
  - low-latency audio
  - automatic language/dialect switching
  - screen announcements
  - lift-to-activate
  - wrap-around navigation
  - rotor gestures and rotor step size
  - proximity-based speakerphone behavior
  - audio output routing
  - TTS engine/settings options
  - long-text sentence mode
  - incoming notification announcements
- `strings_control_sounds.xml`
  - control sounds and vibrations
  - 3D audio settings
  - individual control sound labels
- `strings_sound_themes.xml`
  - sound themes
  - theme installation/removal/export
  - custom sounds and vibration-related UI text
  - Braille keyboard sound labels inside themes
- `strings_direct_touch.xml`
  - Direct touch settings and app-specific direct typing
- `strings_on_device_ai.xml`
  - on-device AI model selection/download/import/storage/memory/GPU/errors
- `strings_pause.xml`
  - pause/resume BackTalk UI
- `strings_radial_menu.xml`
  - circle/radial menu
- `strings_update.xml`
  - built-in updater
- `strings_gemini_api_key.xml`
  - Gemini API key settings
- `strings_gemini_errors.xml`
  - Gemini API and quota/error messages

### Braille IME

Under `braille/brailleime/src/phone/res/values-cs/`:

- `strings_backtalk.xml`
  - screen-toward/tabletop/screen-away orientation announcements
  - charging-port orientation announcements
  - orientation lock/unlock announcements
  - tablet held-up faces-away setting
  - Braille keyboard typing sounds
  - Braille keyboard echo
  - vertical dot swap setting
  - skip tutorial

### Braille common

Under `braille/common/src/phone/res/values-cs/`:

- `strings_backtalk.xml`
  - orientation lock toggle gesture label

## Important commits in the Czech branch

- `276effcbb6825c13dc222706c2d4a74a5c7fd37f` — initial BackTalk-specific Czech strings
- `885c622875751031eb4cd52e5233da6779a22eb9` — initial Braille orientation additions
- `9104fa801add12524d7fa98ed998c6afb19c17e3` — lift activation, wrap-around, rotor gestures, call routing
- `b823d08891ff36c71329a69ff89b70f2639a2aae` — speech and notification settings

Additional feature-specific Czech commits were made for sound themes, control sounds, Direct touch, on-device AI, Pause BackTalk, circle menu, updater, Gemini settings/errors, and Braille keyboard settings.

## Completed BackTalk-specific areas

The Czech branch currently includes translations for:

- sound themes
- control sounds and per-control vibrations UI
- 3D audio
- custom sounds
- screen-away / tabletop / device orientation announcements
- audio routing
- rotor step size and two-finger rotor gestures
- lift-to-activate
- wrap-around navigation
- proximity-based speakerphone behavior
- Direct touch
- on-device AI
- Gemini API key and errors
- Pause BackTalk
- circle/radial menu
- built-in updater
- Braille keyboard additions
- separate TTS options
- sentence-at-a-time long-text mode
- incoming notification announcements

## Still required before declaring 100% coverage

1. Audit BackTalk commits for existing English resource keys whose meaning changed compared with inherited TalkBack Czech translations.
2. Update those existing Czech values in their original files where needed.
3. Check for duplicate resource names across all Czech resource files.
4. Run XML/AAPT/Gradle validation.
5. Build a test APK.
6. Confirm whether the APK package/signing configuration can coexist safely with the system/Google TalkBack before installation testing.
7. Runtime-test the Czech strings on a real device.
8. Send clean incremental pull requests to upstream `trypsynth/backtalk`.

## Maintenance workflow

For every new upstream BackTalk commit or release:

1. Compare upstream changes against the last checked upstream commit recorded here.
2. Inspect changes to English translatable resources under TalkBack and Braille modules.
3. Translate newly added user-visible strings to Czech.
4. Audit modified existing keys for semantic changes and update inherited Czech values when necessary.
5. Preserve placeholders/XLIFF/plurals exactly.
6. Commit changes to `matejplch626-afk/backtalk:czech-translation` with a focused commit message.
7. Update the `Last upstream commit checked` value in this file.
8. Report what was changed and whether a build validation succeeded.
9. When a coherent batch is ready and tested, open a small pull request to `trypsynth/backtalk:master`.

## Upstream contribution policy

Prefer small, reviewable pull requests rather than a permanently open mega-PR. After upstream accepts the initial Czech localization, subsequent BackTalk features should normally be delivered as focused Czech translation updates tied to the relevant upstream changes.
