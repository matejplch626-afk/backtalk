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
- `69d6f06647f92ad8ccfadfcb9eb67ed808809d88` — corrected Czech validation workflow; successful audit/build run followed

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

## Audit and build status as of 2026-10-06

The dedicated GitHub Actions workflow `Czech translation audit and build` completed successfully in run #7.

Successful checks in that run:

- audited changed existing English resource keys
- applied audited Czech semantic updates
- verified no duplicate Czech resource names in the checked resource sets
- validated Czech XML files
- validated simple-string format placeholders
- completed the Gradle debug build successfully
- produced phone and Wear debug APK artifacts

The previous run #6 failed only because the first placeholder validator incorrectly compared plural resources across languages with different plural-form counts. The validator was corrected; run #7 then completed successfully.

The audit also identified a broad upstream branding change from `TalkBack` to `Backtalk` in many inherited strings. These branding-only changes and any remaining semantic changes should be reviewed before the initial upstream Czech PR is considered complete.

## Test APK status

A successful test artifact was produced from GitHub Actions run #7.

Relevant phone APK:

- `backtalk-phone-debug.apk`

Wear build also exists:

- `backtalk-wear-debug.apk`

Application/package configuration has been checked:

- BackTalk application ID: `fyi.quin.backtalk`
- system/Google TalkBack therefore is not replaced by this package
- the test build is expected to install alongside system TalkBack as a separate app/accessibility service
- project build configuration states that published debug builds are signed with a debug key

Current runtime-testing instruction:

1. Install `backtalk-phone-debug.apk`.
2. Keep the existing/system TalkBack installed and enabled initially.
3. Confirm Android completes installation without an error.
4. Open Android accessibility settings and confirm BackTalk appears as a separate accessibility service alongside TalkBack.
5. Report the result before enabling BackTalk for a longer live test.
6. After separation is confirmed, begin a controlled real-device Czech localization test.

## Remaining work before declaring 100% coverage

1. Finish review of remaining changed existing keys found by the audit, especially inherited `TalkBack` -> `Backtalk` branding updates and any true semantic changes.
2. Runtime-test the Czech strings on a real Android device.
3. Correct any terminology, truncation, missing strings, malformed announcements, or feature-specific issues discovered during runtime testing.
4. Re-run XML/resource validation and Gradle build after final corrections.
5. Prepare the initial professional upstream pull request to `trypsynth/backtalk:master`.

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

## Initial professional upstream PR plan

Do not open the first upstream PR until the Czech localization has passed real-device testing and remaining audit findings have been reviewed.

The initial PR should be professional, compact, and easy to review. It should explain that:

- BackTalk already inherits the large Czech localization from Google TalkBack
- this contribution adds and updates Czech strings specifically needed by BackTalk
- new BackTalk-only keys are isolated in feature-specific Czech resource files where practical
- inherited Czech strings are edited only where BackTalk changed the meaning or branding of an existing English key
- Android placeholders, XLIFF markup, plural rules, escaping, and XML semantics were preserved
- the Czech resources passed automated XML/resource validation and a real Gradle debug build
- the localization was tested by a native Czech speaker who is also a daily screen-reader user

Long-term maintenance offer for the upstream developers:

- Matěj Plch is willing to act as the Czech localization maintainer/contact
- upstream developers do not need to translate Czech themselves
- when BackTalk adds or changes user-visible English strings, focused Czech follow-up PRs can be submitted promptly
- the preferred model is one coherent initial Czech PR followed by small incremental maintenance PRs

Suggested wording for the first PR description or accompanying message:

> Czech localization is maintained continuously. I am a native Czech speaker and daily screen reader user. I can keep Backtalk-specific Czech strings updated as new features are added. You don't need to maintain the Czech translations yourself; I will submit small follow-up pull requests whenever English user-facing strings change.

This upstream-maintainer relationship is a project goal and should remain part of future planning.
