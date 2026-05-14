"""\nReusable color palette for TypeFx.

Supports:
    - Foreground colors
    - Background colors
    - Bright colors
    - HEX / RGB colors
    - Reset/Formatting color
    - Hex color conversion
    - Extended named colors

Designed to integrate with TypeFx's text writing functions.
"""

# Reset / Formatting Colors
RESET = "\033[0m"
BOLD = "\033[1m"
BIM = "\033[2m"
UNDERLINE = "\033[4m"
ITALIC = "\033[3m"
BLINK = "\033[5m"
INVERT = "\033[7m"
REVERSE = INVERT
BLINK_FAST = "\033[6m"
BLINK_SLOW = "\033[25m"
CONCEAL = "\033[8m"
STRIKETHROUGH = "\033[9m"
OVERLINE = "\033[53m"
FRAME = "\033[51m"
ENCIRCLE = "\033[52m"
OVERLINE = "\033[53m"
DOUBLE_UNDERLINE = "\033[21m"
CURLY_UNDERLINE = "\033[4:3m"
DOTTED_UNDERLINE = "\033[4:4m"
DASHED_UNDERLINE = "\033[4:5m"
SHADOW = "\033[1:2m"
SUPERSCRIPT = "\033[73m"
SUBSCRIPT = "\033[74m"
BRIGHT = "\033[1m"
BRIGHT_FOREGROUND = "\033[9m"
BRIGHT_BACKGROUND = "\033[10m"
BRIGHT_HEX = "\033[10m"

# Foreground Colors (Basic)
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GRAY = "\033[90m"

# Foreground Colors (Bright)
BRIGHT_BLACK = GRAY
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background Colors (Basic)
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_GRAY = "\033[100m"

# Background Colors (Bright)
BG_BRIGHT_BLACK = BG_GRAY
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

# Extended Named Foreground Colors
ORANGE = "\033[38;2;255;165;0m"
PURPLE = "\033[38;2;128;0;128m"
PINK = "\033[38;2;255;105;180m"
TEAL = "\033[38;2;0;128;128m"
VIOLET = "\033[38;2;148;0;211m"
TURQUOISE = "\033[38;2;64;224;208m"
LIME = "\033[38;2;50;205;50m"
GOLD = "\033[38;2;255;215;0m"
SILVER = "\033[38;2;192;192;192m"
MARRON = "\033[38;2;128;0;0m"
NAVY = "\033[38;2;0;0;128m"
OLIVE = "\033[38;2;128;128;0m"
CORAL = "\033[38;2;255;127;80m"
SKYBLUE = "\033[38;2;135;206;235m"
AQUA = "\033[38;2;0;255;255m"
INDIGO = "\033[38;2;75;0;130m"
BROWN = "\033[38;2;139;69;19m"
AMBER = "\033[38;2;255;191;0m"
CRIMSON = "\033[38;2;220;20;60m"
SALMON = "\033[38;2;250;128;114m"
PLUM = "\033[38;2;221;160;221m"
SLATE = "\033[38;2;112;128;144m"
TOMATO = "\033[38;2;255;99;71m"
CHOCOLATE = "\033[38;2;210;105;30m"
PEACH = "\033[38;2;255;218;185m"
MINT = "\033[38;2;189;252;201m"
LAVENDER_BLUSH = "\033[38;2;255;240;245m"
CORNFLOWER = "\033[38;2;100;149;237m"
SPRING_GREEN = "\033[38;2;0;255;127m"
SEA_GREEN = "\033[38;2;46;139;87m"
STEEL_BLUE = "\033[38;2;70;130;180m"
DODGER_BLUE = "\033[38;2;30;144;255m"
DARK_ORCHID = "\033[38;2;153;50;204m"
SIENNA = "\033[38;2;160;82;45m"
SADDLE_BROWN = "\033[38;2;139;69;19m"
PERU = "\033[38;2;205;133;63m"
ROSY_BROWN = "\033[38;2;188;143;143m"
KHAKI = "\033[38;2;240;230;140m"
BEIGE = "\033[38;2;245;245;220m"
IVORY = "\033[38;2;255;255;240m"
CHARCOAL = "\033[38;2;54;69;79m"

# Extended Named Background Colors
BG_ORANGE = "\033[48;2;255;165;0m"
BG_PURPLE = "\033[48;2;128;0;128m"
BG_PINK = "\033[48;2;255;105;180m"
BG_TEAL = "\033[48;2;0;128;128m"
BG_VIOLET = "\033[48;2;148;0;211m"
BG_TURQUOISE = "\033[48;2;64;224;208m"
BG_LIME = "\033[48;2;50;205;50m"
BG_GOLD = "\033[48;2;255;215;0m"
BG_SILVER = "\033[48;2;192;192;192m"
BG_MARRON = "\033[48;2;128;0;0m"
BG_NAVY = "\033[48;2;0;0;128m"
BG_OLIVE = "\033[48;2;128;128;0m"
BG_CORAL = "\033[48;2;255;127;80m"
BG_SKYBLUE = "\033[48;2;135;206;235m"
BG_AQUA = "\033[48;2;0;255;255m"
BG_INDIGO = "\033[48;2;75;0;130m"
BG_BROWN = "\033[48;2;139;69;19m"
BG_AMBER = "\033[48;2;255;191;0m"
BG_CRIMSON = "\033[48;2;220;20;60m"
BG_SALMON = "\033[48;2;250;128;114m"
BG_PLUM = "\033[48;2;221;160;221m"
BG_SLATE = "\033[48;2;112;128;144m"
BG_TOMATO = "\033[48;2;255;99;71m"
BG_CHOCOLATE = "\033[48;2;210;105;30m"
BG_PEACH = "\033[48;2;255;218;185m"
BG_MINT = "\033[48;2;189;252;201m"
BG_CORNFLOWER = "\033[48;2;100;149;237m"
BG_SPRING_GREEN = "\033[48;2;0;255;127m"
BG_SEA_GREEN = "\033[48;2;46;139;87m"
BG_STEEL_BLUE = "\033[48;2;70;130;180m"
BG_DODGER_BLUE = "\033[48;2;30;144;255m"
BG_DARK_ORCHID = "\033[48;2;153;50;204m"
BG_SIENNA = "\033[48;2;160;82;45m"
BG_PERU = "\033[48;2;205;133;63m"
BG_ROSY_BROWN = "\033[48;2;188;143;143m"
BG_KHAKI = "\033[48;2;240;230;140m"
BG_CHARCOAL = "\033[48;2;54;69;79m"

# Gradient / Nature Colors
LEAF_GREEN = "\033[38;2;34;139;34m"
GRASS_GREEN = "\033[38;2;124;252;0m"
MOSS_GREEN = "\033[38;2;85;107;47m"
FERN_GREEN = "\033[38;2;79;121;66m"
PINE_GREEN = "\033[38;2;1;68;33m"
SAGE_GREEN = "\033[38;2;154;174;121m"
OLIVE_DRAB = "\033[38;2;107;142;35m"
FOREST_GREEN = "\033[38;2;34;139;34m"

SOIL_BROWN = "\033[38;2;101;67;33m"
BARK_BROWN = "\033[38;2;139;69;19m"
CLAY_BROWN = "\033[38;2;150;75;0m"
TAUPE = "\033[38;2;72;60;50m"
TAN = "\033[38;2;210;180;140m"
WALNUT = "\033[38;2;95;58;32m"

SUNFLOWER = "\033[38;2;255;215;0m"
ROSE_PINK = "\033[38;2;255;99;132m"
LAVENDER = "\033[38;2;181;126;220m"
PETAL_RED = "\033[38;2;220;20;60m"
LILAC = "\033[38;2;200;162;200m"
ORCHID = "\033[38;2;218;112;214m"
FUCHSIA = "\033[38;2;255;0;255m"
MAUVE = "\033[38;2;224;176;255m"

SKY_BLUE = "\033[38;2;135;206;235m"
CLOUD_WHITE = "\033[38;2;245;245;245m"
RAIN_GRAY = "\033[38;2;176;196;222m"
MIDNIGHT_BLUE = "\033[38;2;25;25;112m"
CERULEAN = "\033[38;2;0;123;167m"
AZURE = "\033[38;2;240;255;255m"
CRANBERRY = "\033[38;2;143;0;35m"
WINE = "\033[38;2;114;47;55m"

# ANSI 8-bit / 256-color helpers
def fg_256(n: int) -> str:
    return f"\033[38;5;{n}m"

def bg_256(n: int) -> str:
    return f"\033[48;5;{n}m"

# =========================
# Preset Palettes
# =========================
PALETTES = {
    "SUCCESS": ["#2ECC71", "#27AE60", "#1E8449"],
    "ERROR": ["#E74C3C", "#C0392B", "#922B21"],
    "WARNING": ["#F1C40F", "#F39C12", "#D68910"],
    "INFO": ["#3498DB", "#2980B9", "#1F618D"],
    "NEON": ["#39FF14", "#FF00FF", "#00FFFF", "#FFFF00"],
    "PASTEL": ["#FFB6C1", "#B0E0E6", "#98FB98", "#E6E6FA"],
    "OCEAN": ["#0077B6", "#00B4D8", "#90E0EF", "#CAF0F8"],
    "SUNSET": ["#FF6B6B", "#FFA07A", "#FFD93D", "#6BCB77"],
    "FOREST": ["#1B4332", "#2D6A4F", "#40916C", "#52B788"],
    "GARDEN": [
        "#228B22",
        "#7CFC00",
        "#FFDB58",
        "#FF6384",
        "#87CEEB",
        "#654321",
        "#B57EDC",
    ],
    "CYBER": ["#00FF41", "#FF00FF", "#00FFFF", "#FFFF00", "#FF6600"],
    "NOIR": ["#1A1A1A", "#333333", "#666666", "#999999", "#CCCCCC"],
    "ROSE": ["#FFE4E1", "#FFC0CB", "#FF69B4", "#DB7093", "#C71585"],
}


# HEX & RGB Helpers
def hex_to_ansi(hex_color: str) -> str:
    """
    Converts a HEX color string to an ANSI foreground escape code.

    Parameters
    ----------
    hex_color : str
        The HEX color string (e.g. "#RRGGBB" or "RRGGBB").

    Returns
    -------
    str
        ANSI 24-bit color escape code for the given hex value.

    Examples
    --------
    >>> hex_to_ansi("#FFFFFF")
    '\\033[38;2;255;255;255m'
    >>> hex_to_ansi("000000")
    '\\033[38;2;0;0;0m'
    """
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m"


def bg_hex_to_ansi(hex_color: str) -> str:
    """
    Converts a HEX color string to an ANSI background escape code.

    Parameters
    ----------
    hex_color : str
        The HEX color string (e.g. "#RRGGBB" or "RRGGBB").

    Returns
    -------
    str
        ANSI 24-bit background color escape code.

    Examples
    --------
    >>> bg_hex_to_ansi("#000000")
    '\\033[48;2;0;0;0m'
    >>> bg_hex_to_ansi("FFFFFF")
    '\\033[48;2;255;255;255m'
    """
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
    return f"\033[48;2;{r};{g};{b}m"


def rgb_to_ansi(r: int, g: int, b: int) -> str:
    """
    Converts RGB values to an ANSI foreground escape code.

    Parameters
    ----------
    r : int
        Red component (0-255).
    g : int
        Green component (0-255).
    b : int
        Blue component (0-255).

    Returns
    -------
    str
        ANSI 24-bit foreground color escape code.

    Examples
    --------
    >>> rgb_to_ansi(255, 255, 255)
    '\\033[38;2;255;255;255m'
    >>> rgb_to_ansi(0, 0, 0)
    '\\033[38;2;0;0;0m'
    """
    return f"\033[38;2;{r};{g};{b}m"

def bg_rgb_to_ansi(r: int, g: int, b: int) -> str:
    """
    Converts RGB values to an ANSI background escape code.

    Parameters
    ----------
    r : int
        Red component (0-255).
    g : int
        Green component (0-255).
    b : int
        Blue component (0-255).

    Returns
    -------
    str
        ANSI 24-bit background color escape code.

    Examples
    --------
    >>> bg_rgb_to_ansi(0, 0, 0)
    '\\033[48;2;0;0;0m'
    >>> bg_rgb_to_ansi(255, 255, 255)
    '\\033[48;2;255;255;255m'
    """
    return f"\033[48;2;{r};{g};{b}m"


# Utility Combiners
def colorize(text: str, *style: str) -> str:
    """
    Applies one or more ANSI style codes to a text string.

    Parameters
    ----------
    text : str
        The text to style.
    *style : str
        Variable number of ANSI escape codes to apply.

    Returns
    -------
    str
        Styled text with ANSI reset appended.

    Examples
    --------
    >>> from typefx.colors import RED, BOLD
    >>> colorize("Hello", RED)
    '\\033[31mHello\\033[0m'
    >>> colorize("World", RED, BOLD)
    '\\033[31m\\033[1mWorld\\033[0m'
    """
    return "".join(style) + text + RESET