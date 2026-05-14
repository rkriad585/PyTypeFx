from typefx.colors import (
    BG_BRIGHT_BLACK,
    BG_GRAY,
    BRIGHT_BLACK,
    GRAY,
    INVERT,
    RESET,
    REVERSE,
    bg_hex_to_ansi,
    bg_rgb_to_ansi,
    colorize,
    hex_to_ansi,
    rgb_to_ansi,
)


def test_hex_to_ansi():
    assert hex_to_ansi("#FFFFFF") == "\033[38;2;255;255;255m"
    assert hex_to_ansi("000000") == "\033[38;2;0;0;0m"
    assert hex_to_ansi("#FF0000") == "\033[38;2;255;0;0m"


def test_bg_hex_to_ansi():
    assert bg_hex_to_ansi("#000000") == "\033[48;2;0;0;0m"
    assert bg_hex_to_ansi("FFFFFF") == "\033[48;2;255;255;255m"


def test_rgb_to_ansi():
    assert rgb_to_ansi(255, 255, 255) == "\033[38;2;255;255;255m"
    assert rgb_to_ansi(0, 0, 0) == "\033[38;2;0;0;0m"


def test_bg_rgb_to_ansi():
    assert bg_rgb_to_ansi(0, 0, 0) == "\033[48;2;0;0;0m"
    assert bg_rgb_to_ansi(255, 255, 255) == "\033[48;2;255;255;255m"


def test_colorize():
    from typefx.colors import RED, BOLD

    result = colorize("Hello", RED)
    assert result == "\033[31mHello\033[0m"

    result = colorize("World", RED, BOLD)
    assert result == "\033[31m\033[1mWorld\033[0m"


def test_colorize_no_style():
    assert colorize("plain") == "plain" + RESET


def test_ansi_constants_unique():
    assert RESET == "\033[0m"
    assert INVERT == "\033[7m"
    assert REVERSE == "\033[7m"
    assert GRAY == "\033[90m"
    assert BRIGHT_BLACK == "\033[90m"
    assert BG_GRAY == "\033[100m"
    assert BG_BRIGHT_BLACK == "\033[100m"


def test_new_format_codes():
    from typefx.colors import (
        CONCEAL,
        CURLY_UNDERLINE,
        DASHED_UNDERLINE,
        DOTTED_UNDERLINE,
        DOUBLE_UNDERLINE,
        ENCIRCLE,
        FRAME,
        OVERLINE,
        SHADOW,
        STRIKETHROUGH,
        SUBSCRIPT,
        SUPERSCRIPT,
    )
    assert CONCEAL == "\033[8m"
    assert STRIKETHROUGH == "\033[9m"
    assert OVERLINE == "\033[53m"
    assert FRAME == "\033[51m"
    assert ENCIRCLE == "\033[52m"
    assert DOUBLE_UNDERLINE == "\033[21m"
    assert CURLY_UNDERLINE == "\033[4:3m"
    assert DOTTED_UNDERLINE == "\033[4:4m"
    assert DASHED_UNDERLINE == "\033[4:5m"
    assert SHADOW == "\033[1:2m"
    assert SUPERSCRIPT == "\033[73m"
    assert SUBSCRIPT == "\033[74m"


def test_new_foreground_colors():
    from typefx.colors import AMBER, CRIMSON, SALMON, PLUM, SLATE, TOMATO, CHOCOLATE
    assert AMBER == "\033[38;2;255;191;0m"
    assert CRIMSON == "\033[38;2;220;20;60m"
    assert SALMON == "\033[38;2;250;128;114m"
    assert PLUM == "\033[38;2;221;160;221m"
    assert SLATE == "\033[38;2;112;128;144m"
    assert TOMATO == "\033[38;2;255;99;71m"
    assert CHOCOLATE == "\033[38;2;210;105;30m"


def test_new_background_colors():
    from typefx.colors import BG_AMBER, BG_CRIMSON, BG_SALMON, BG_PLUM, BG_SLATE, BG_TOMATO, BG_KHAKI
    assert BG_AMBER == "\033[48;2;255;191;0m"
    assert BG_CRIMSON == "\033[48;2;220;20;60m"
    assert BG_SALMON == "\033[48;2;250;128;114m"
    assert BG_PLUM == "\033[48;2;221;160;221m"
    assert BG_SLATE == "\033[48;2;112;128;144m"
    assert BG_TOMATO == "\033[48;2;255;99;71m"
    assert BG_KHAKI == "\033[48;2;240;230;140m"


def test_fg_256():
    from typefx.colors import fg_256
    assert fg_256(0) == "\033[38;5;0m"
    assert fg_256(255) == "\033[38;5;255m"
    assert fg_256(196) == "\033[38;5;196m"


def test_bg_256():
    from typefx.colors import bg_256
    assert bg_256(0) == "\033[48;5;0m"
    assert bg_256(255) == "\033[48;5;255m"
    assert bg_256(196) == "\033[48;5;196m"


def test_new_palettes():
    from typefx.colors import PALETTES
    assert "OCEAN" in PALETTES
    assert "SUNSET" in PALETTES
    assert "FOREST" in PALETTES
    assert "CYBER" in PALETTES
    assert "NOIR" in PALETTES
    assert "ROSE" in PALETTES
    assert len(PALETTES["OCEAN"]) == 4
    assert len(PALETTES["CYBER"]) == 5


def test_new_gradient_colors():
    from typefx.colors import PINE_GREEN, SAGE_GREEN, LILAC, FUCHSIA, MIDNIGHT_BLUE, WALNUT
    assert PINE_GREEN == "\033[38;2;1;68;33m"
    assert SAGE_GREEN == "\033[38;2;154;174;121m"
    assert LILAC == "\033[38;2;200;162;200m"
    assert FUCHSIA == "\033[38;2;255;0;255m"
    assert MIDNIGHT_BLUE == "\033[38;2;25;25;112m"
    assert WALNUT == "\033[38;2;95;58;32m"
