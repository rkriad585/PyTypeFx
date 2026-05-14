import os
import random
import sys
import time

from typefx._types import Position
from typefx.colors import PALETTES, hex_to_ansi, rgb_to_ansi
from typefx.constant import HEX_RANDOM, RESET, RGB_COLORS


# Colors converting functions
def supports_ansi() -> bool:
    """
    Checks whether the current terminal supports ANSI escape codes.

    On Windows, checks for Windows Terminal session or a TTY.
    On other platforms, checks if stdout is a TTY.

    Parameters
    ----------
    None

    Returns
    -------
    bool
        True if ANSI escape codes are supported, False otherwise.

    Examples
    --------
    >>> supports_ansi()
    True
    """
    if sys.platform.startswith("win"):
        return "WT_SESSION" in os.environ or sys.stdout.isatty()
    return sys.stdout.isatty()


def write(char: str) -> None:
    """
    Writes a string to stdout and flushes the buffer.

    Parameters
    ----------
    char : str
        The character or string to write.

    Returns
    -------
    None

    Examples
    --------
    >>> write("Hi")
    """
    sys.stdout.write(char)
    sys.stdout.flush()


def _cursor_left(n: int = 1) -> str:
    """
    Returns a backspace escape string to move the cursor left.

    On non-TTY outputs (piped/redirected), returns an empty string
    to avoid corrupting output.

    Parameters
    ----------
    n : int, optional
        Number of positions to move left. Defaults to 1.

    Returns
    -------
    str
        Backspace characters or empty string on non-TTY.

    Examples
    --------
    >>> _cursor_left(1)
    '\\b'
    """
    if not sys.stdout.isatty():
        return ""
    return "\b" * n


def _clear_line(length: int) -> str:
    """
    Returns an escape string to clear a given number of characters.

    Works by backspacing, overwriting with spaces, then backspacing again.
    Returns empty string on non-TTY outputs.

    Parameters
    ----------
    length : int
        Number of characters to clear.

    Returns
    -------
    str
        Escape sequence to clear characters, or empty on non-TTY.

    Examples
    --------
    >>> _clear_line(3)
    '\\b\\b\\b   \\b\\b\\b'
    """
    if not sys.stdout.isatty():
        return ""
    return "\b" * length + " " * length + "\b" * length


def _make_delay(base_delay: float, speed: str):
    """
    Creates a delay-calculating function based on speed setting.

    Internal helper for the @typefx decorator. Returns a callable that
    takes a character and returns a per-character delay in seconds
    adjusted for punctuation and random jitter.

    Parameters
    ----------
    base_delay : float
        The base delay value in seconds.
    speed : str
        Speed modifier: "fast", "slow", "normal", "random", or "none".

    Returns
    -------
    callable
        Function ``(char) -> float`` returning delay in seconds.

    Examples
    --------
    >>> fn = _make_delay(0.1, "fast")
    >>> fn("a") >= 0
    True
    """
    base: float = float(base_delay)
    speed = (speed or "normal").lower()
    if speed == "fast":
        factor = 0.5
        return lambda c: max(0, base * factor + random.uniform(0, base * 0.06))
    elif speed == "slow":
        factor = 1.8
        return lambda c: base * factor + random.uniform(0, base * 0.06)
    elif speed == "random":
        return lambda c: base + random.uniform(0.3, 1.8)
    elif speed == "none":
        return lambda c: 0
    return lambda c: base + random.uniform(0, base * 0.06)


def _make_color(hex_colors):
    """
    Creates a color-resolving function from a color specification.

    Internal helper for the @typefx decorator. Returns a callable
    ``(char, index) -> str`` that provides ANSI codes per character
    based on hex strings, lists, or palette names.

    Parameters
    ----------
    hex_colors : str, list, tuple, or None
        Color definition: hex string, list of hex strings, or palette
        name ("rainbow", "random", "SUCCESS", etc.).

    Returns
    -------
    callable or None
        Function ``(char, index) -> str`` returning ANSI code, or None.

    Examples
    --------
    >>> fn = _make_color("#FF0000")
    >>> fn("a", 0)
    '\\033[38;2;255;0;0m'
    """
    if not hex_colors:
        return None

    if isinstance(hex_colors, str):
        key = hex_colors.upper()
        if key in PALETTES:
            palette = PALETTES[key]
            ansi_list = [hex_to_ansi(h) for h in palette]
            return lambda c, i: ansi_list[i % len(ansi_list)]

        if hex_colors.lower() == "rainbow":
            ansi_list = [f"\033[38;2;{r};{g};{b}m" for r, g, b in RGB_COLORS]
            return lambda c, i: ansi_list[i % len(ansi_list)]
        if hex_colors.lower() == "random":
            return lambda c, i: hex_to_ansi(random.choice(HEX_RANDOM))

        try:
            ansi = hex_to_ansi(hex_colors)
            return lambda c, i: ansi
        except Exception:
            return None

    if isinstance(hex_colors, (list, tuple)) and hex_colors:
        ansi_list = [hex_to_ansi(h) for h in hex_colors]
        return lambda c, i: ansi_list[i % len(ansi_list)]

    return None


def _type_out_text(text: str, delay_fn, color_fn=None):
    """
    Writes text with per-character delay and optional coloring.

    Internal helper used by the @typefx decorator. Prints characters
    sequentially using a delay function and optional color callback.

    Parameters
    ----------
    text : str
        The text to output.
    delay_fn : callable
        Function taking a character and returning delay in seconds.
    color_fn : callable, optional
        Function taking (char, index) and returning ANSI color code.

    Examples
    --------
    >>> _type_out_text("Hi", lambda c: 0, None)
    """
    if not text:
        return

    first_delay = delay_fn(text[0])

    if first_delay <= 0:
        if color_fn:
            out = "".join(
                f"{color_fn(ch, i)}{ch}{RESET}" for i, ch in enumerate(text)
            )
        else:
            out = text
        sys.stdout.write(out)
    else:
        for i, ch in enumerate(text):
            if color_fn:
                ansi = color_fn(ch, i)
                sys.stdout.write(f"{ansi}{ch}{RESET}")
            else:
                sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay_fn(ch))
    if not text.endswith("\n"):
        sys.stdout.write("\n")
    sys.stdout.flush()


def _hex_to_rgb(hex_color: str):
    """
    Converts a HEX color string to an (R, G, B) tuple.

    Parameters
    ----------
    hex_color : str
        HEX color string, with or without leading "#".

    Returns
    -------
    tuple
        (R, G, B) tuple of integers in range 0-255.

    Examples
    --------
    >>> _hex_to_rgb("#FF0000")
    (255, 0, 0)
    """
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def gradient(text: str, start_hex: str, end_hex: str):
    """
    Applies a smooth color gradient across a string of text.

    Each character is colored with an interpolated RGB value between
    start_hex and end_hex, producing a seamless color transition.

    Parameters
    ----------
    text : str
        The text to colorize.
    start_hex : str
        Starting HEX color (e.g. "#FF0000").
    end_hex : str
        Ending HEX color (e.g. "#0000FF").

    Returns
    -------
    str
        Text with per-character ANSI color codes and trailing RESET.

    Examples
    --------
    >>> gradient("AB", "#FF0000", "#0000FF")
    '\\033[38;2;255;0;0mA\\033[38;2;0;0;255mB\\033[0m'
    """

    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    if not text:
        return text

    start_r, start_g, start_b = hex_to_rgb(start_hex)
    end_r, end_g, end_b = hex_to_rgb(end_hex)
    length = len(text) - 1 if len(text) > 1 else 1
    result = ""

    for i, char in enumerate(text):
        ratio = i / length
        r = int(start_r + (end_r - start_r) * ratio)
        g = int(start_g + (end_g - start_g) * ratio)
        b = int(start_b + (end_b - start_b) * ratio)
        result += f"{rgb_to_ansi(r, g, b)}{char}"
    return result + RESET


def _resolve_to_ansi_list(color_input):
    """
    Resolves a flexible color input into a list of ANSI color codes.

    Accepts various input types:
    - A single ANSI code string (starts with ``\\033[``)
    - A hex color string (``#RRGGBB`` or ``RRGGBB``)
    - A palette name (``"SUCCESS"``, ``"NEON"``, etc.)
    - ``"rainbow"`` — returns the predefined rainbow color list
    - ``"random"`` — returns None (random color per character at runtime)
    - A list or tuple of any of the above

    Parameters
    ----------
    color_input : str, list, tuple, or None
        The color specification to resolve.

    Returns
    -------
    list of str or None
        A list of ANSI escape codes, or None for random/no color.

    Examples
    --------
    >>> _resolve_to_ansi_list("#FF0000")
    ['\\033[38;2;255;0;0m']
    >>> _resolve_to_ansi_list("rainbow")
    ['\\033[38;2;255;0;0m', ...]
    >>> _resolve_to_ansi_list(None) is None
    True
    """
    if color_input is None:
        return None
    if isinstance(color_input, str):
        if color_input.startswith("\033["):
            return [color_input]
        if color_input.startswith("#") or (
            len(color_input) == 6
            and all(c in "0123456789ABCDEFabcdef" for c in color_input)
        ):
            return [hex_to_ansi(color_input)]
        key = color_input.upper()
        if key in PALETTES:
            return [hex_to_ansi(h) for h in PALETTES[key]]
        if color_input.lower() == "rainbow":
            return [f"\033[38;2;{r};{g};{b}m" for r, g, b in RGB_COLORS]
        if color_input.lower() == "random":
            return None
        return None
    if isinstance(color_input, (list, tuple)):
        result = []
        for item in color_input:
            resolved = _resolve_to_ansi_list(item)
            if resolved:
                result.extend(resolved)
        return result if result else None
    return None


def _position_prefix(text_length: int, position: Position = "left") -> str:
    """
    Returns an ANSI positioning prefix for text alignment.

    Supports four positions: "left" (default, no change), "right" (right-aligns
    using terminal width), "top" (moves cursor to first line), and "bottom"
    (moves cursor to last line).

    Parameters
    ----------
    text_length : int
        Length of the text to position.
    position : str, optional
        One of "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    str
        ANSI escape sequence or space padding for the requested position.
        Returns empty string for "left".

    Examples
    --------
    >>> _position_prefix(5, "left")
    ''
    >>> _position_prefix(5, "right").startswith(" ")
    True
    """
    if position == "left":
        return ""
    if position == "right":
        import shutil
        width = shutil.get_terminal_size().columns
        padding = max(0, width - text_length)
        return " " * padding
    if position == "top":
        return "\033[H"
    if position == "bottom":
        import shutil
        height = shutil.get_terminal_size().lines
        return f"\033[{height};1H"
    return ""


def _make_style(*styles: str) -> str:
    """
    Joins multiple ANSI style codes into a single string.

    Internal helper that concatenates style constants like BOLD, UNDERLINE
    into one ANSI prefix applied before text output.

    Parameters
    ----------
    *styles : str
        Variable number of ANSI escape code strings.

    Returns
    -------
    str
        Concatenated ANSI style string.

    Examples
    --------
    >>> _make_style("\\033[1m", "\\033[4m")
    '\\033[1m\\033[4m'
    """
    return "".join(styles)