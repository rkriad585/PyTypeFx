from typefx.constant import RESET
from typefx.utility import (
    _clear_line,
    _cursor_left,
    _hex_to_rgb,
    _make_color,
    _make_delay,
    gradient,
    hex_to_ansi,
    rgb_to_ansi,
    supports_ansi,
    write,
)


def test_gradient():
    result = gradient("AB", "#FF0000", "#0000FF")
    assert "\033[38;2;255;0;0m" in result
    assert "\033[38;2;0;0;255m" in result
    assert RESET in result


def test_gradient_empty():
    assert gradient("", "#000000", "#FFFFFF") == ""


def test_gradient_single_char():
    result = gradient("X", "#FF0000", "#0000FF")
    assert "\033[38;2;255;0;0mX" in result


def test_hex_to_rgb():
    assert _hex_to_rgb("#FF0000") == (255, 0, 0)
    assert _hex_to_rgb("00FF00") == (0, 255, 0)


def test_make_delay_fast():
    fn = _make_delay(0.1, "fast")
    delay = fn("a")
    assert 0 <= delay <= 0.1


def test_make_delay_slow():
    fn = _make_delay(0.1, "slow")
    delay = fn("a")
    assert delay >= 0.18


def test_make_delay_normal():
    fn = _make_delay(0.1, "normal")
    delay = fn("a")
    assert delay >= 0


def test_make_delay_none():
    fn = _make_delay(0.1, "none")
    assert fn("a") == 0


def test_make_color_none():
    assert _make_color(None) is None
    assert _make_color("") is None


def test_make_color_single_hex():
    fn = _make_color("#FF0000")
    assert fn is not None
    assert fn("a", 0) == "\033[38;2;255;0;0m"


def test_make_color_list():
    fn = _make_color(["#FF0000", "#00FF00"])
    assert fn is not None
    assert fn("a", 0) == "\033[38;2;255;0;0m"
    assert fn("b", 1) == "\033[38;2;0;255;0m"
    assert fn("c", 2) == "\033[38;2;255;0;0m"


def test_make_color_rainbow():
    fn = _make_color("rainbow")
    assert fn is not None
    assert "38;2" in fn("a", 0)


def test_make_color_random():
    fn = _make_color("random")
    assert fn is not None
    assert "38;2" in fn("a", 0)


def test_make_color_palette():
    fn = _make_color("SUCCESS")
    assert fn is not None
    assert "38;2" in fn("a", 0)


def test_write(capsys):
    write("H")
    out, _ = capsys.readouterr()
    assert out == "H"


def test_supports_ansi():
    result = supports_ansi()
    assert isinstance(result, bool)


def test_cursor_left_tty():
    result = _cursor_left(1)
    assert result == "\b" or result == ""


def test_clear_line_tty():
    result = _clear_line(3)
    assert result == "\b\b\b   \b\b\b" or result == ""
