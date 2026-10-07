#!/usr/bin/env python3
"""Apply Backtalk semantic updates to inherited Czech TalkBack resources.

This deliberately edits only named <string> values. It fails if a key is missing
or appears more than once, so upstream resource changes cannot be silently hidden.
"""
from pathlib import Path
import re
import sys


def replace_strings(path: str, replacements: dict[str, str]) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    for key, value in replacements.items():
        pattern = re.compile(
            rf'(<string\s+name="{re.escape(key)}"[^>]*>)(.*?)(</string>)',
            re.DOTALL,
        )
        text, count = pattern.subn(lambda m: m.group(1) + value + m.group(3), text)
        if count != 1:
            raise SystemExit(f"{path}: expected exactly one {key!r}, found {count}")
    p.write_text(text, encoding="utf-8")


def add_string_if_missing(path: str, key: str, value: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if re.search(rf'<string\s+name="{re.escape(key)}"(?=[\s>])', text):
        return
    marker = "</resources>"
    if text.count(marker) != 1:
        raise SystemExit(f"{path}: unexpected resources root")
    addition = f'    <string name="{key}">{value}</string>\n'
    text = text.replace(marker, addition + marker)
    p.write_text(text, encoding="utf-8")


replace_strings(
    "talkback/src/main/res/values-cs/strings.xml",
    {
        "pref_reduce_window_delay_title": "Vypnout animace",
        "summary_pref_verbose_scroll_announcement": "Po každém posunutí říkat, které položky jsou zobrazené",
        "summary_pref_count_repeated_symbols": "Říkat, kolikrát se symbol opakuje, pokud se opakuje čtyřikrát nebo více",
        "summary_pref_a11y_hints": "Po popisu položky říkat, jak ji použít",
        "summary_speak_container_element_positions": "Říkat, když vstoupíte do seznamu, mřížky nebo jiného kontejneru nebo je opustíte",
        "pref_speak_roles_title": "Číst typ položky",
        "pref_speak_roles_summary": "Například tlačítko nebo zaškrtávací políčko",
        "summary_pref_speak_element_ids": "Říkat ID tlačítek, která nemají štítek",
        "title_pref_category_reduce_latency_summary": "Tato nastavení zrychlují reakce Backtalku po dotyku obrazovky",
        "title_pref_category_manage_focus_indicator": "Indikátor výběru",
        "summary_pref_show_exit_watermark": "Při zapnutí Backtalku zobrazit, jak jej vypnout",
        "pref_node_desc_order_title": "Pořadí podrobností položky",
        "talkback_latency_reduction_summary": "Zrychlit reakce Backtalku po dotyku obrazovky",
        "title_pref_typing_confirmation": "Způsob psaní",
        "message_pref_touch_explore_latency": "Kratší prodleva způsobí, že Backtalk začne mluvit dříve po dotyku klávesnice.\\n\\nZvolte prodlevu",
        "title_pref_gemini_enabled": "Hlasové příkazy Gemini",
        "message_pref_touch_focus_latency": "Kratší prodleva způsobí, že Backtalk začne mluvit dříve po dotyku obrazovky",
        "title_pref_talkback_speech_rate": "Rychlost řeči",
        "pref_auto_enter_table_navigation_title": "V tabulkách přepnout na navigaci v tabulce",
        "title_switch_text_formatting": "Číst formátování textu",
        "pref_category_context_menu_summary": "Klepněte třemi prsty nebo přejeďte nahoru či dolů a potom doprava.",
        "pref_category_context_menu_summary_single_finger": "Přejeďte dolů a potom doprava.",
        "pref_category_selector_menu_summary": "Otáčením dvěma prsty jako číselníkem nebo přejetím třemi prsty doleva či doprava zvolte ovládání čtení. Potom ho změňte přejetím nahoru nebo dolů.",
        "pref_category_selector_menu_summary_single_finger": "Přejetím nahoru a potom dolů nebo dolů a potom nahoru zvolte ovládání čtení. Potom ho změňte přejetím nahoru nebo dolů.",
    },
)

replace_strings(
    "braille/brailleime/src/phone/res/values-cs/strings.xml",
    {
        "title_pref_reverse_dots": "Prohodit levé a pravé body",
        "summary_pref_reverse_dots": "Body 1, 2 a 3 si vymění místa s body 4, 5 a 6",
    },
)

for key, value in {
    "pref_category_selector_menu_summary_no_rotor": "Přejetím třemi prsty doleva nebo doprava zvolte ovládání čtení. Potom ho změňte přejetím nahoru nebo dolů.",
    "title_pref_multi_tap_timeout": "Doba mezi klepnutími",
    "value_multi_tap_timeout_100ms": "0,1 sekundy",
    "value_multi_tap_timeout_150ms": "0,15 sekundy",
    "value_multi_tap_timeout_200ms": "0,2 sekundy",
    "value_multi_tap_timeout_250ms": "0,25 sekundy (výchozí)",
    "title_pref_brightness": "Jas",
    "summary_support_change_brightness": "Zvýšit nebo snížit jas obrazovky, i když je obrazovka skrytá",
    "title_pref_shortcut_3finger_4tap": "Čtyřikrát klepnout třemi prsty",
}.items():
    add_string_if_missing(
        "talkback/src/main/res/values-cs/strings_backtalk.xml",
        key,
        value,
    )

print("Applied Czech semantic updates successfully.")
