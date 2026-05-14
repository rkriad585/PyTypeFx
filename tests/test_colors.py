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
