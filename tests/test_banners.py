from typefx.banners import (
    banner_arrow,
    banner_block,
    banner_dash,
    box,
    divider,
    project_banner,
    rule,
    section_header,
)
from typefx.colors import BRIGHT_CYAN, CYAN


def test_box_single():
    result = box("Hello")
    assert result.startswith("┌")
    assert result.endswith("┘")
    assert "Hello" in result


def test_box_double():
    result = box("Test", style="double")
    assert result.startswith("╔")
    assert "Test" in result
    assert result.endswith("╝")


def test_box_rounded():
    result = box("Hi", style="rounded")
    assert result.startswith("╭")
    assert result.endswith("╯")


def test_box_heavy():
    result = box("Hi", style="heavy")
    assert result.startswith("┏")
    assert result.endswith("┛")


def test_box_ascii():
    result = box("Hi", style="ascii")
    assert result.startswith("+")
    assert "+" in result


def test_box_multiline():
    result = box("Line1\nLine2")
    assert "Line1" in result
    assert "Line2" in result


def test_box_with_title():
    result = box("Content", title="Title")
    assert "Title" in result
    assert "Content" in result


def test_divider_default():
    result = divider()
    assert result == "━" * 40


def test_divider_custom_char():
    result = divider(char="=", length=20)
    assert result == "=" * 20


def test_divider_with_label():
    result = divider(label="Section")
    assert "Section" in result
    assert len(result) == 40


def test_banner_block():
    result = banner_block("Hello")
    assert "Hello" in result
    assert result.startswith("┏")
    assert "┃" in result


def test_banner_arrow():
    result = banner_arrow("Hello")
    assert "Hello" in result
    assert "▸▸" in result


def test_banner_dash():
    result = banner_dash("Hello")
    assert "Hello" in result
    assert "──" in result


def test_section_header():
    result = section_header("My Section")
    assert "My Section" in result
    assert "─" in result


def test_project_banner():
    result = project_banner("MyApp", tagline="Awesome", version="1.0")
    assert "MyApp" in result
    assert "Awesome" in result
    assert "1.0" in result
    assert result.startswith("╔")
    assert result.endswith("╝")


def test_project_banner_minimal():
    result = project_banner("Minimal")
    assert "Minimal" in result
    assert "╔" in result


def test_rule():
    result = rule()
    assert CYAN in result
    assert "━" in result
    assert len(result) > 50


def test_rule_custom():
    result = rule(color=BRIGHT_CYAN, char="=")
    assert BRIGHT_CYAN in result
    assert "=" in result


def test_kaomoji_default():
    from typefx.banners import kaomoji, KAOMOJI, ALL_KAOMOJI, kaomoji_list, kaomoji_categories
    result = kaomoji()
    assert isinstance(result, str)
    assert len(result) > 0
    assert result in ALL_KAOMOJI


def test_kaomoji_by_category():
    from typefx.banners import kaomoji, KAOMOJI
    for cat in KAOMOJI:
        result = kaomoji(cat)
        assert result in KAOMOJI[cat]


def test_kaomoji_list():
    from typefx.banners import kaomoji_list, KAOMOJI
    assert len(kaomoji_list("happy")) > 0
    assert "happy" in kaomoji_list() or len(kaomoji_list()) > 0
    for cat in KAOMOJI:
        lst = kaomoji_list(cat)
        assert all(k in KAOMOJI[cat] for k in lst)


def test_kaomoji_categories():
    from typefx.banners import kaomoji_categories, KAOMOJI
    cats = kaomoji_categories()
    assert len(cats) == len(KAOMOJI)
    assert "happy" in cats
    assert "sad" in cats


def test_animal_default():
    from typefx.banners import animal, ANIMALS, ANIMAL_NAMES
    result = animal()
    assert isinstance(result, str)
    assert len(result) > 0
    assert result in list(ANIMALS.values())


def test_animal_by_name():
    from typefx.banners import animal, ANIMALS
    for name in ANIMALS:
        result = animal(name)
        assert result == ANIMALS[name]


def test_animal_names():
    from typefx.banners import animal_names, ANIMALS
    names = animal_names()
    assert len(names) == len(ANIMALS)
    assert "cat1" in names
    assert "dog1" in names


def test_animal_specific():
    from typefx.banners import animal
    cat = animal("cat1")
    assert "|\\__/" in cat or "(((" in cat
    dog = animal("dog1")
    assert "|o  o  o|" in dog


def test_emoji_default():
    from typefx.banners import emoji, EMOJI, ALL_EMOJI_NAMES
    result = emoji()
    assert isinstance(result, str)
    assert result in list(EMOJI.values())


def test_emoji_by_name():
    from typefx.banners import emoji, EMOJI
    for name in EMOJI:
        result = emoji(name)
        assert result == EMOJI[name]


def test_emoji_names():
    from typefx.banners import emoji_names, EMOJI
    names = emoji_names()
    assert len(names) == len(EMOJI)
    assert "heart" in names
    assert "star" in names


def test_buddy():
    from typefx.banners import buddy
    result = buddy("MyApp")
    assert "MyApp" in result
    assert len(result) > 10


def test_buddy_with_animal():
    from typefx.banners import buddy
    result = buddy("MyApp", animal_name="cat1")
    assert "MyApp" in result
    assert "|\\__/" in result or "(((" in result


def test_buddy_box():
    from typefx.banners import buddy_box
    result = buddy_box("MyApp")
    assert "MyApp" in result
    assert "╭" in result or "┌" in result


def test_color_art():
    from typefx.banners import color_art
    from typefx.colors import GREEN, RESET
    result = color_art("hello", GREEN)
    assert GREEN in result
    assert "hello" in result
    assert RESET in result


def test_box_with_color():
    from typefx.colors import GREEN
    result = box("Hello", color=GREEN)
    assert GREEN in result
    assert "Hello" in result


def test_box_with_align():
    result = box("Hi", align="center", width=20)
    assert "Hi" in result


def test_box_with_padding():
    result = box("Hi", padding=1)
    assert "Hi" in result
    lines = result.split("\n")
    assert len(lines) >= 4  # top + padding + content + padding + bottom


def test_box_with_border_color():
    from typefx.colors import CYAN
    result = box("Hi", border_color=CYAN)
    assert CYAN in result


def test_hero_banner():
    from typefx.banners import hero_banner
    result = hero_banner("Welcome")
    assert "Welcome" in result
    assert "★" in result
    assert "┏" in result


def test_alert_banner():
    from typefx.banners import alert_banner
    result = alert_banner("Something happened", level="info")
    assert "Something happened" in result
    assert "INFO" in result


def test_alert_banner_error():
    from typefx.banners import alert_banner
    result = alert_banner("Error!", level="error")
    assert "Error!" in result


def test_alert_banner_success():
    from typefx.banners import alert_banner
    result = alert_banner("Done!", level="success")
    assert "Done!" in result


def test_alert_banner_warning():
    from typefx.banners import alert_banner
    result = alert_banner("Caution", level="warning")
    assert "Caution" in result


def test_progress_bar():
    from typefx.banners import progress_bar
    result = progress_bar(pct=50, width=10)
    assert "50%" in result
    assert "[" in result


def test_progress_bar_custom():
    from typefx.banners import progress_bar
    result = progress_bar(pct=100, width=5, label="Download")
    assert "100%" in result
    assert "Download" in result


def test_progress_bar_zero():
    from typefx.banners import progress_bar
    result = progress_bar(pct=0, width=10)
    assert "0%" in result


def test_tag():
    from typefx.banners import tag
    result = tag("INFO")
    assert "INFO" in result
    assert "[" in result
    assert "]" in result


def test_tag_custom_bracket():
    from typefx.banners import tag
    result = tag("OK", bracket="round")
    assert "(" in result
    assert ")" in result


def test_tag_invert():
    from typefx.banners import tag
    result = tag("WARN", invert=True)
    assert "WARN" in result


def test_frame():
    from typefx.banners import frame
    result = frame("art")
    assert "art" in result
    assert "╭" in result


def test_centered_banner():
    from typefx.banners import centered_banner
    result = centered_banner("Title")
    assert "Title" in result
    assert "─" in result


def test_buddy_multi():
    from typefx.banners import buddy_multi
    result = buddy_multi("MyApp", animal_names=["cat1", "dog1"])
    assert "MyApp" in result
    assert "|\\__/" in result or "(((" in result


def test_buddy_with_params():
    from typefx.banners import buddy
    from typefx.colors import GREEN
    result = buddy("App", align="center", message="Hello!", message_color=GREEN)
    assert "App" in result
    assert "Hello!" in result


def test_buddy_no_name():
    from typefx.banners import buddy
    result = buddy("Secret", show_name=False)
    assert "Secret" not in result


def test_divider_with_color():
    from typefx.banners import divider
    from typefx.colors import GREEN
    result = divider(color=GREEN)
    assert GREEN in result
    assert "━" in result


def test_divider_align_left():
    from typefx.banners import divider
    result = divider(label="Start", align="left", length=40)
    assert "Start" in result


def test_rule_with_length():
    from typefx.banners import rule
    from typefx.colors import GREEN
    result = rule(color=GREEN, length=30)
    assert GREEN in result
    assert "━" in result


def test_section_header_align():
    from typefx.banners import section_header
    result = section_header("Centered", align="center")
    assert "Centered" in result


def test_kaomoji_new_categories():
    from typefx.banners import kaomoji, KAOMOJI
    assert "greeting" in KAOMOJI
    assert "wave" in KAOMOJI
    assert "hug" in KAOMOJI
    assert "sorry" in KAOMOJI
    assert "thank" in KAOMOJI
    assert "excited" in KAOMOJI
    assert "magic" in KAOMOJI
    assert "food" in KAOMOJI
    for cat in ["greeting", "wave", "hug"]:
        result = kaomoji(cat)
        assert result in KAOMOJI[cat]


def test_animal_new_names():
    from typefx.banners import animal, ANIMALS
    assert "lion" in ANIMALS
    assert "horse" in ANIMALS
    assert "cow" in ANIMALS
    assert "sheep" in ANIMALS
    assert "elephant" in ANIMALS
    assert "whale" in ANIMALS
    assert "dolphin" in ANIMALS
    assert "shark" in ANIMALS
    assert "snake" in ANIMALS
    assert "butterfly" in ANIMALS
    assert "wolf" in ANIMALS
    assert "dragon" in ANIMALS
    for name in ["lion", "horse", "cow", "sheep", "elephant"]:
        result = animal(name)
        assert result == ANIMALS[name]


def test_emoji_new_entries():
    from typefx.banners import EMOJI
    assert "heart_bold" in EMOJI
    assert "zodiac_aries" in EMOJI
    assert "chess_king" in EMOJI
    assert "math_sqrt" in EMOJI
    assert "degree" in EMOJI
    assert "star_sparkle" in EMOJI
    assert "check_heavy" in EMOJI


def test_color_art_with_params():
    from typefx.banners import color_art
    from typefx.colors import GREEN
    result = color_art("hello", GREEN, align="center", width=20)
    assert "hello" in result
