from typefx.colors import (
    BOLD,
    CYAN,
    GREEN,
    ITALIC,
    RED,
    RESET,
    UNDERLINE,
    YELLOW,
)
from typefx.styles import (
    ERROR,
    GHOST,
    INFO,
    KEYWORD,
    SUCCESS,
    TITLE,
    WARNING,
    apply_style,
    compose,
)


def test_error_style():
    assert ERROR["color"] == RED
    assert BOLD in ERROR["style"]


def test_success_style():
    assert SUCCESS["color"] == GREEN
    assert BOLD in SUCCESS["style"]


def test_warning_style():
    assert WARNING["color"] == YELLOW
    assert BOLD in WARNING["style"]


def test_info_style():
    assert INFO["color"] == CYAN
    assert ITALIC in INFO["style"]


def test_title_style():
    assert TITLE["color"] is not None
    assert BOLD in TITLE["style"]
    assert UNDERLINE in TITLE["style"]


def test_ghost_style_no_color():
    assert "color" not in GHOST or GHOST["color"] is None


def test_apply_style_info():
    result = apply_style("test", INFO)
    assert CYAN in result
    assert ITALIC in result
    assert "test" in result
    assert result.endswith(RESET)


def test_apply_style_error():
    result = apply_style("fail", ERROR)
    assert RED in result
    assert BOLD in result
    assert "fail" in result
    assert result.endswith(RESET)


def test_compose():
    style = compose(RED, BOLD, UNDERLINE)
    assert style["color"] == RED
    assert BOLD in style["style"]
    assert UNDERLINE in style["style"]


def test_compose_no_color():
    style = compose(None, BOLD)
    assert "color" not in style or style["color"] is None
    assert BOLD in style["style"]


def test_compose_no_formats():
    style = compose(RED)
    assert style["color"] == RED
    assert "style" not in style


def test_apply_style_with_compose():
    style = compose(RED, BOLD)
    result = apply_style("X", style)
    assert RED in result
    assert BOLD in result
    assert result == f"{BOLD}{RED}X{RESET}"


def test_keyword_style():
    assert BOLD in KEYWORD["style"]


def test_style_unpack_in_writer(capsys, mock_sleep):
    from typefx.writers import TypeWriter
    result = TypeWriter("Hi", delay=0.001, **SUCCESS)
    assert result == 2
    out, _ = capsys.readouterr()
    assert GREEN in out
    assert BOLD in out


def test_tip_style():
    from typefx.styles import TIP
    from typefx.colors import BRIGHT_GREEN, ITALIC
    assert TIP["color"] == BRIGHT_GREEN
    assert ITALIC in TIP["style"]


def test_danger_style():
    from typefx.styles import DANGER
    from typefx.colors import BRIGHT_RED, BOLD, BLINK
    assert DANGER["color"] == BRIGHT_RED
    assert BOLD in DANGER["style"]
    assert BLINK in DANGER["style"]


def test_primary_style():
    from typefx.styles import PRIMARY
    from typefx.colors import BRIGHT_BLUE, BOLD
    assert PRIMARY["color"] == BRIGHT_BLUE
    assert BOLD in PRIMARY["style"]


def test_accent_style():
    from typefx.styles import ACCENT
    from typefx.colors import BRIGHT_MAGENTA, BOLD
    assert ACCENT["color"] == BRIGHT_MAGENTA
    assert BOLD in ACCENT["style"]


def test_banner_style():
    from typefx.styles import BANNER
    from typefx.colors import BRIGHT_CYAN, BOLD, OVERLINE, UNDERLINE
    assert BANNER["color"] == BRIGHT_CYAN
    assert BOLD in BANNER["style"]
    assert OVERLINE in BANNER["style"]
    assert UNDERLINE in BANNER["style"]


def test_caption_style():
    from typefx.styles import CAPTION
    from typefx.colors import BRIGHT_BLACK, ITALIC
    assert CAPTION["color"] == BRIGHT_BLACK
    assert ITALIC in CAPTION["style"]


def test_tag_style():
    from typefx.styles import TAG
    from typefx.colors import BRIGHT_MAGENTA, BIM, INVERT
    assert TAG["color"] == BRIGHT_MAGENTA
    assert BIM in TAG["style"]
    assert INVERT in TAG["style"]


def test_log_style():
    from typefx.styles import LOG
    from typefx.colors import BRIGHT_BLACK
    assert LOG["color"] == BRIGHT_BLACK
    assert "style" not in LOG


def test_verbose_style():
    from typefx.styles import VERBOSE
    from typefx.colors import BRIGHT_BLACK, BIM, ITALIC
    assert VERBOSE["color"] == BRIGHT_BLACK
    assert ITALIC in VERBOSE["style"]
    assert BIM in VERBOSE["style"]


def test_strikethrough_style():
    from typefx.styles import STRIKETHROUGH
    from typefx.colors import STRIKETHROUGH as STRIKETHROUGH_ANSI
    assert "color" not in STRIKETHROUGH or STRIKETHROUGH["color"] is None
    assert STRIKETHROUGH_ANSI in STRIKETHROUGH["style"]


def test_bold_style():
    from typefx.styles import BOLD_STYLE
    from typefx.colors import BOLD
    assert "color" not in BOLD_STYLE or BOLD_STYLE["color"] is None
    assert BOLD in BOLD_STYLE["style"]


def test_hint_style():
    from typefx.styles import HINT
    from typefx.colors import BRIGHT_CYAN, BIM, ITALIC
    assert HINT["color"] == BRIGHT_CYAN
    assert BIM in HINT["style"]
    assert ITALIC in HINT["style"]


def test_meta_style():
    from typefx.styles import META
    from typefx.colors import BRIGHT_BLUE, ITALIC
    assert META["color"] == BRIGHT_BLUE
    assert ITALIC in META["style"]


def test_section_style():
    from typefx.styles import SECTION
    from typefx.colors import CYAN, BOLD, DOUBLE_UNDERLINE
    assert SECTION["color"] == CYAN
    assert BOLD in SECTION["style"]
    assert DOUBLE_UNDERLINE in SECTION["style"]


def test_box_title_style():
    from typefx.styles import BOX_TITLE
    from typefx.colors import BRIGHT_CYAN, BOLD, UNDERLINE
    assert BOX_TITLE["color"] == BRIGHT_CYAN
    assert BOLD in BOX_TITLE["style"]
    assert UNDERLINE in BOX_TITLE["style"]


def test_box_error_style():
    from typefx.styles import BOX_ERROR
    from typefx.colors import RED, BOLD, INVERT
    assert BOX_ERROR["color"] == RED
    assert BOLD in BOX_ERROR["style"]
    assert INVERT in BOX_ERROR["style"]


def test_box_success_style():
    from typefx.styles import BOX_SUCCESS
    from typefx.colors import GREEN, BOLD, INVERT
    assert BOX_SUCCESS["color"] == GREEN
    assert BOLD in BOX_SUCCESS["style"]
    assert INVERT in BOX_SUCCESS["style"]


def test_separator_style():
    from typefx.styles import SEPARATOR
    from typefx.colors import BRIGHT_BLACK, BIM
    assert SEPARATOR["color"] == BRIGHT_BLACK
    assert BIM in SEPARATOR["style"]


def test_anchor_style():
    from typefx.styles import ANCHOR
    from typefx.colors import BRIGHT_CYAN, UNDERLINE
    assert ANCHOR["color"] == BRIGHT_CYAN
    assert UNDERLINE in ANCHOR["style"]
