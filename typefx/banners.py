from typing import List, Optional

from typefx.colors import BOLD, BRIGHT_CYAN, BRIGHT_WHITE, CYAN, GREEN, RESET, YELLOW
from typefx.styles import apply_style


_BLOCK = ["█", "▓", "▒", "░"]
_DOTS = ["⣀", "⣄", "⣤", "⣦", "⣶", "⣾", "⣿"]
_ARROW_HEADS = ["▸", "▹", "►", "‣", "›"]
_SEPARATORS = ["━", "─", "═", "▔", "▁", "░", "▒", "▓"]

BOX_STYLES = {
    "single": {"tl": "┌", "tr": "┐", "bl": "└", "br": "┘", "h": "─", "v": "│"},
    "double": {"tl": "╔", "tr": "╗", "bl": "╚", "br": "╝", "h": "═", "v": "║"},
    "rounded": {"tl": "╭", "tr": "╮", "bl": "╰", "br": "╯", "h": "─", "v": "│"},
    "heavy": {"tl": "┏", "tr": "┓", "bl": "┗", "br": "┛", "h": "━", "v": "┃"},
    "ascii": {"tl": "+", "tr": "+", "bl": "+", "br": "+", "h": "-", "v": "|"},
    "double_h": {"tl": "╓", "tr": "╖", "bl": "╙", "br": "╜", "h": "═", "v": "│"},
    "double_v": {"tl": "╒", "tr": "╕", "bl": "╘", "br": "╛", "h": "─", "v": "║"},
}


def box(text: str, style: str = "single", title: Optional[str] = None) -> str:
    s = BOX_STYLES.get(style, BOX_STYLES["single"])
    lines = text.split("\n")
    inner_w = max(len(l) for l in lines)
    top = s["tl"] + s["h"] * (inner_w + 2) + s["tr"]
    bot = s["bl"] + s["h"] * (inner_w + 2) + s["br"]
    body = "\n".join(s["v"] + " " + l.ljust(inner_w) + " " + s["v"] for l in lines)
    if title:
        title_str = f" {title} "
        insert_at = (inner_w + 2) - len(title_str)
        if insert_at > 1:
            top = top[:1] + title_str + s["h"] * insert_at + top[-1:]
        else:
            top = top[:1] + title_str[:(inner_w + 2)] + top[-1:]
    return top + "\n" + body + "\n" + bot


def divider(char: str = "━", length: int = 40, label: Optional[str] = None) -> str:
    if label:
        label = f" {label} "
        side = (length - len(label)) // 2
        return char * side + label + char * (length - side - len(label))
    return char * length


def banner_block(text: str, color: str = BRIGHT_CYAN, bold: bool = True) -> str:
    style_code = BOLD if bold else ""
    styled = f"{style_code}{color}{text}{RESET}"
    top = f"┏{'━' * (len(text) + 2)}┓"
    mid = f"┃ {styled} ┃"
    bot = f"┗{'━' * (len(text) + 2)}┛"
    return top + "\n" + mid + "\n" + bot


def banner_arrow(text: str, color: str = BRIGHT_CYAN) -> str:
    styled = f"{BOLD}{color}{text}{RESET}"
    return f"  ▏{styled}  ▸▸"


def banner_dash(text: str, color: str = BRIGHT_WHITE) -> str:
    styled = f"{BOLD}{color}{text}{RESET}"
    return f"── {styled} ──"


def section_header(text: str, width: int = 50, color: str = CYAN) -> str:
    styled = f"{BOLD}{color}{text}{RESET}"
    line = "─" * width
    return f"\n{line}\n  {styled}\n{line}"


def project_banner(
    name: str,
    tagline: Optional[str] = None,
    version: Optional[str] = None,
    color: str = BRIGHT_CYAN,
    accent: str = GREEN,
    width: int = 40,
) -> str:
    name_styled = f"{BOLD}{color}{name}{RESET}"
    top = f"╔{'═' * (width - 2)}╗"
    name_line = f"║{name_styled:^{width - 1}}║"
    lines = [top, name_line]
    if tagline:
        tag_styled = f"{accent}{tagline}{RESET}"
        lines.append(f"║ {tag_styled:<{width - 3}} ║")
    if version:
        ver_styled = f"{YELLOW}v{version}{RESET}"
        lines.append(f"║{ver_styled:>{width - 1}}║")
    bot = f"╚{'═' * (width - 2)}╝"
    lines.append(bot)
    return "\n".join(lines)


def rule(color: str = CYAN, char: str = "━") -> str:
    return f"{color}{char * 50}{RESET}"
