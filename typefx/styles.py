"""
Predefined text styles for TypeFx.

Each style is a dict with optional ``"color"`` and ``"style"`` keys
that can be unpacked (``**style``) directly into any writer function.

Examples
--------
>>> from typefx.styles import ERROR, SUCCESS, TITLE
>>> from typefx.writers import TypeWriter
>>> TypeWriter("Error!", **ERROR)
>>> TypeWriter("Success!", **SUCCESS)
>>> TypeWriter("Title", **TITLE)
"""

from typing import Dict, Tuple, Union

from typefx.colors import (
    BIM,
    BLACK,
    BLINK,
    BLUE,
    BOLD,
    BRIGHT_BLACK,
    BRIGHT_BLUE,
    BRIGHT_CYAN,
    BRIGHT_GREEN,
    BRIGHT_MAGENTA,
    BRIGHT_RED,
    BRIGHT_WHITE,
    BRIGHT_YELLOW,
    CYAN,
    GREEN,
    INVERT,
    ITALIC,
    MAGENTA,
    OVERLINE,
    RED,
    STRIKETHROUGH as STRIKETHROUGH_ANSI,
    UNDERLINE,
    WHITE,
    YELLOW,
)


def compose(color=None, *formats: str) -> Dict[str, Union[str, Tuple[str, ...]]]:
    """
    Creates a style dict from an optional color and format codes.

    Parameters
    ----------
    color : str, optional
        ANSI color code (e.g. RED, GREEN) or None.
    *formats : str
        ANSI format codes (e.g. BOLD, UNDERLINE).

    Returns
    -------
    dict
        Style dict with ``"color"`` and/or ``"style"`` keys.

    Examples
    --------
    >>> from typefx.colors import RED, BOLD
    >>> compose(RED, BOLD)
    {'color': '\\033[31m', 'style': ('\\033[1m',)}
    """
    result: Dict[str, Union[str, Tuple[str, ...]]] = {}
    if color is not None:
        result["color"] = color
    if formats:
        result["style"] = formats
    return result


def apply_style(text: str, style: dict) -> str:
    """
    Applies a style dict directly to a string and returns ANSI-wrapped text.

    Parameters
    ----------
    text : str
        The text to style.
    style : dict
        A style dict with optional ``"color"`` and/or ``"style"`` keys.

    Returns
    -------
    str
        The text wrapped in ANSI codes with a trailing RESET.

    Examples
    --------
    >>> from typefx.colors import RED, BOLD
    >>> styled = apply_style("Error!", {"color": RED, "style": (BOLD,)})
    >>> "\\033[1m" in styled and "\\033[31m" in styled
    True
    """
    from typefx.colors import RESET as _RESET
    from typefx.utility import _make_style
    prefix = _make_style(*style.get("style", ()))
    color = style.get("color", "")
    return f"{prefix}{color}{text}{_RESET}"


# ──────────────────────────────────────────────
# Preset Styles — dicts that can be **unpacked
# into any writer function
# ──────────────────────────────────────────────

# ── Feedback / Status ──
ERROR = compose(RED, BOLD)
SUCCESS = compose(GREEN, BOLD)
WARNING = compose(YELLOW, BOLD)
INFO = compose(CYAN, ITALIC)

# ── Typography ──
TITLE = compose(BRIGHT_WHITE, BOLD, UNDERLINE)
HEADING = compose(BRIGHT_CYAN, BOLD)
SUBHEADING = compose(BRIGHT_BLUE, ITALIC)
CODE = compose(BRIGHT_GREEN, ITALIC)
KEYWORD = compose(BRIGHT_MAGENTA, BOLD)
LINK = compose(BRIGHT_CYAN, UNDERLINE)
QUOTE = compose(WHITE, ITALIC)
DIM = compose(None, BIM)
HIGHLIGHT = compose(YELLOW, BOLD, INVERT)
STRIKETHROUGH = compose(None, STRIKETHROUGH_ANSI)
CAPTION = compose(BRIGHT_BLACK, ITALIC)
LABEL = compose(BRIGHT_CYAN, BIM)
TAG = compose(BRIGHT_MAGENTA, BIM, INVERT)
BOLD_STYLE = compose(None, BOLD)
UNDERLINE_STYLE = compose(None, UNDERLINE)
OVERLINE_STYLE = compose(None, OVERLINE)

# ── Themed ──
NEON = compose(None, BOLD, BRIGHT_MAGENTA, BRIGHT_CYAN)
GHOST = compose(None, BIM)
MUTED = compose(BLACK, BIM)
PUNCH = compose(BRIGHT_WHITE, BOLD, INVERT)
EMPHASIS = compose(BRIGHT_YELLOW, BOLD, UNDERLINE)
BANNER = compose(BRIGHT_CYAN, BOLD, OVERLINE, UNDERLINE)

# ── Semantic / Feedback ──
DEBUG = compose(BRIGHT_BLACK, BIM)
TRACE = compose(BRIGHT_BLACK, ITALIC)
CRITICAL = compose(BRIGHT_RED, BOLD, INVERT)
IMPORTANT = compose(BRIGHT_YELLOW, BOLD, UNDERLINE)
NOTE = compose(BLUE, ITALIC)
TIP = compose(BRIGHT_GREEN, ITALIC)
HINT = compose(BRIGHT_CYAN, BIM, ITALIC)
DANGER = compose(BRIGHT_RED, BOLD, BLINK)
LOG = compose(BRIGHT_BLACK)
VERBOSE = compose(BRIGHT_BLACK, ITALIC, BIM)
META = compose(BRIGHT_BLUE, ITALIC)
PRIMARY = compose(BRIGHT_BLUE, BOLD)
SECONDARY = compose(WHITE, BIM)
ACCENT = compose(BRIGHT_MAGENTA, BOLD)
