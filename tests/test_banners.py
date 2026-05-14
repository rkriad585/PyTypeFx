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
