import random
from typing import Dict, List, Optional, Union

from typefx.colors import BOLD, BRIGHT_CYAN, BRIGHT_WHITE, CYAN, GREEN, RESET, YELLOW
from typefx.styles import apply_style


# ── Utility helpers ──

def _apply_color(text: str, color: Optional[str] = None) -> str:
    if color:
        return f"{color}{text}{RESET}"
    return text


def _pad_text(text: str, padding: int = 0) -> str:
    if padding <= 0:
        return text
    lines = text.split("\n")
    if not lines:
        return text
    max_w = max(len(l) for l in lines)
    space = " " * padding
    pad_line = " " * (max_w + 2 * padding)
    padded = [space + l + space for l in lines]
    spacer = [pad_line] * padding
    return "\n".join(spacer + padded + spacer)


def _align_text(text: str, width: int, align: str = "left") -> str:
    lines = text.split("\n")
    result = []
    for line in lines:
        if align == "center":
            result.append(line.center(width))
        elif align == "right":
            result.append(line.rjust(width))
        else:
            result.append(line.ljust(width))
    return "\n".join(result)


def _measure(text: str) -> int:
    return max(len(l) for l in text.split("\n"))


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


def box(
    text: str,
    style: str = "single",
    title: Optional[str] = None,
    color: Optional[str] = None,
    align: str = "left",
    padding: int = 0,
    width: Optional[int] = None,
    border_color: Optional[str] = None,
    title_color: Optional[str] = None,
) -> str:
    s = BOX_STYLES.get(style, BOX_STYLES["single"])
    text = _pad_text(text, padding)
    lines = text.split("\n")
    inner_w = max(len(l) for l in lines) if lines else 0
    if width is not None and width > inner_w:
        inner_w = width
    aligned = _align_text("\n".join(lines), inner_w, align).split("\n")
    bc = border_color or ""
    tl = f"{bc}{s['tl']}{RESET}" if bc else s["tl"]
    tr = f"{bc}{s['tr']}{RESET}" if bc else s["tr"]
    bl_ = f"{bc}{s['bl']}{RESET}" if bc else s["bl"]
    br = f"{bc}{s['br']}{RESET}" if bc else s["br"]
    h = f"{bc}{s['h']}{RESET}" if bc else s["h"]
    v = f"{bc}{s['v']}{RESET}" if bc else s["v"]
    top = tl + h * (inner_w + 2) + tr
    bot = bl_ + h * (inner_w + 2) + br
    body_lines = []
    for l in aligned:
        styled = _apply_color(l, color)
        body_lines.append(f"{v} {styled} {v}")
    body = "\n".join(body_lines)
    if title:
        title_str = f" {title} "
        if title_color:
            title_str = f"{title_color}{title_str}{RESET}"
        if bc:
            title_str = f"{bc}{title_str}{RESET}"
        insert_at = (inner_w + 2) - len(title_str) + (len(title_color or "") + len(RESET)) * bool(title_color) + (len(bc) + len(RESET)) * bool(bc and title_color) - 2
        raw_insert = (inner_w + 2) - len(title_str)
        if raw_insert > 1:
            top = top[:1] + title_str + h * raw_insert + top[-1:]
        else:
            top = top[:1] + title_str[:(inner_w + 2)] + top[-1:]
    return top + "\n" + body + "\n" + bot


def divider(
    char: str = "━",
    length: int = 40,
    label: Optional[str] = None,
    color: Optional[str] = None,
    align: str = "center",
) -> str:
    if label:
        label_text = f" {label} "
        if color:
            label_text = f"{color}{label_text}{RESET}"
        raw_len = len(label)
        if align == "left":
            return label_text + char * (length - raw_len - 2)
        elif align == "right":
            return char * (length - raw_len - 2) + label_text
        side = (length - raw_len - 2) // 2
        return char * side + label_text + char * (length - side - raw_len - 2)
    result = char * length
    if color:
        result = f"{color}{result}{RESET}"
    return result


def banner_block(
    text: str,
    color: str = BRIGHT_CYAN,
    bold: bool = True,
    align: str = "center",
    padding: int = 0,
    width: Optional[int] = None,
    box_style: str = "heavy",
    border_color: Optional[str] = None,
    bg_color: Optional[str] = None,
) -> str:
    style_code = BOLD if bold else ""
    content = style_code + color + text + RESET
    if bg_color:
        content = bg_color + content + RESET
    inner_w = len(text)
    if width and width > inner_w:
        inner_w = width
    if align == "center":
        content = content.center(inner_w + 2 + len(style_code) + len(color) + len(RESET) * 1)
    s = BOX_STYLES.get(box_style, BOX_STYLES["single"])
    bc = border_color or ""
    tl = f"{bc}{s['tl']}{RESET}" if bc else s["tl"]
    tr = f"{bc}{s['tr']}{RESET}" if bc else s["tr"]
    bl_ = f"{bc}{s['bl']}{RESET}" if bc else s["bl"]
    br = f"{bc}{s['br']}{RESET}" if bc else s["br"]
    h = f"{bc}{s['h']}{RESET}" if bc else s["h"]
    v = f"{bc}{s['v']}{RESET}" if bc else s["v"]
    top = tl + h * (inner_w + 2) + tr
    mid = f"{v} {content} {v}"
    bot = bl_ + h * (inner_w + 2) + br
    return top + "\n" + mid + "\n" + bot


def banner_arrow(
    text: str,
    color: str = BRIGHT_CYAN,
    bold: bool = True,
    arrow_char: str = "▸",
    align: str = "left",
    padding: int = 0,
    width: Optional[int] = None,
) -> str:
    style_code = BOLD if bold else ""
    styled = f"{style_code}{color}{text}{RESET}"
    pad = " " * padding
    if width:
        text_len = len(text) + 4
        filler = " " if align == "right" else " "
        return f"{pad}{' ' * (width - text_len) if align == 'right' else ''}  {pad}{styled}  {arrow_char}{arrow_char}"
    if align == "right":
        return f"{pad}{'  '}{styled}  {arrow_char}{arrow_char}"
    return f"  {pad}{styled}  {arrow_char}{arrow_char}"


def banner_dash(
    text: str,
    color: str = BRIGHT_WHITE,
    bold: bool = True,
    dash_char: str = "─",
    align: str = "center",
    width: Optional[int] = None,
) -> str:
    style_code = BOLD if bold else ""
    styled = f"{style_code}{color}{text}{RESET}"
    if width:
        side = (width - len(text) - 4) // 2
        return dash_char * side + f"  {styled}  " + dash_char * (width - side - len(text) - 4)
    return f"{dash_char}{dash_char} {styled} {dash_char}{dash_char}"


def section_header(
    text: str,
    width: int = 50,
    color: str = CYAN,
    align: str = "left",
    char: str = "─",
    padding: int = 0,
    bottom_line: bool = True,
) -> str:
    styled = f"{BOLD}{color}{text}{RESET}"
    pad = "\n" * padding
    line = char * width
    if align == "center":
        header = f"\n{line}\n{styled.center(width)}\n{line if bottom_line else ''}"
    elif align == "right":
        header = f"\n{line}\n{styled.rjust(width)}\n{line if bottom_line else ''}"
    else:
        header = f"\n{line}\n  {styled}\n{line if bottom_line else ''}"
    return header + pad


def project_banner(
    name: str,
    tagline: Optional[str] = None,
    version: Optional[str] = None,
    color: str = BRIGHT_CYAN,
    accent: str = GREEN,
    width: int = 40,
    align: str = "center",
    border_style: str = "double",
    border_color: Optional[str] = None,
) -> str:
    name_styled = f"{BOLD}{color}{name}{RESET}"
    s = BOX_STYLES.get(border_style, BOX_STYLES["double"])
    bc = border_color or ""
    tl = f"{bc}{s['tl']}{RESET}" if bc else s["tl"]
    tr = f"{bc}{s['tr']}{RESET}" if bc else s["tr"]
    bl_ = f"{bc}{s['bl']}{RESET}" if bc else s["bl"]
    br = f"{bc}{s['br']}{RESET}" if bc else s["br"]
    h = f"{bc}{s['h']}{RESET}" if bc else s["h"]
    v = f"{bc}{s['v']}{RESET}" if bc else s["v"]
    top = tl + h * (width - 2) + tr
    if align == "center":
        name_line = f"{v}{name_styled:^{width - 1}}{v}"
    elif align == "right":
        name_line = f"{v}{name_styled:>{width - 1}}{v}"
    else:
        name_line = f"{v} {name_styled:<{width - 3}} {v}"
    lines = [top, name_line]
    if tagline:
        tag_styled = f"{accent}{tagline}{RESET}"
        lines.append(f"{v} {tag_styled:<{width - 3}} {v}")
    if version:
        ver_styled = f"{YELLOW}v{version}{RESET}"
        lines.append(f"{v}{ver_styled:>{width - 1}}{v}")
    bot = bl_ + h * (width - 2) + br
    lines.append(bot)
    return "\n".join(lines)


def rule(
    color: str = CYAN,
    char: str = "━",
    length: int = 50,
    label: Optional[str] = None,
) -> str:
    if label:
        label_text = f" {label} "
        styled_label = f"{BOLD}{color}{label_text}{RESET}"
        side = (length - len(label_text)) // 2
        return f"{color}{char * side}{RESET}{styled_label}{color}{char * (length - side - len(label_text))}{RESET}"
    return f"{color}{char * length}{RESET}"


def color_art(
    art: str,
    color: str = BRIGHT_CYAN,
    bg_color: Optional[str] = None,
    align: str = "left",
    padding: int = 0,
    width: Optional[int] = None,
) -> str:
    lines = art.split("\n")
    if width:
        total_color = color + (bg_color or "")
        colored = "\n".join(f"{total_color}{l.center(width) if align == 'center' else l.rjust(width) if align == 'right' else l.ljust(width)}{RESET}" for l in lines)
    else:
        colored = "\n".join(f"{color}{l}{RESET}" for l in lines)
    if padding:
        inner_w = max(len(l) for l in colored.split("\n"))
        pad_line = " " * (inner_w + 2 * padding)
        space = " " * padding
        lines2 = colored.split("\n")
        lines2 = [space + l + space for l in lines2]
        spacer = [pad_line] * padding
        colored = "\n".join(spacer + lines2 + spacer)
    return colored


# ── New Banner Functions ──

def hero_banner(
    text: str,
    color: str = BRIGHT_CYAN,
    width: int = 60,
    accent_char: str = "★",
    align: str = "center",
    border_style: str = "heavy",
    padding: int = 0,
) -> str:
    styled = f"{BOLD}{color}{text}{RESET}"
    ac = f"{color}{accent_char}{RESET}"
    s = BOX_STYLES.get(border_style, BOX_STYLES["heavy"])
    tl = f"{color}{s['tl']}{RESET}"
    tr = f"{color}{s['tr']}{RESET}"
    bl_ = f"{color}{s['bl']}{RESET}"
    br = f"{color}{s['br']}{RESET}"
    h = f"{color}{s['h']}{RESET}"
    v = f"{color}{s['v']}{RESET}"
    inner_w = width - 4
    top = tl + h * (width - 2) + tr
    accent_line = f"{v} {ac} {h * (inner_w - 2)} {ac} {v}"
    if align == "center":
        text_line = f"{v} {styled:^{inner_w}} {v}"
    elif align == "right":
        text_line = f"{v} {styled:>{inner_w}} {v}"
    else:
        text_line = f"{v} {styled:<{inner_w}} {v}"
    bot = bl_ + h * (width - 2) + br
    pad = "\n".join([f"{v} {' ' * inner_w} {v}"] * padding) if padding else ""
    parts = [top]
    if pad:
        parts.append(pad)
    parts.append(accent_line)
    parts.append(text_line)
    parts.append(accent_line)
    if pad:
        parts.append(pad)
    parts.append(bot)
    return "\n".join(parts)


ALERT_STYLES = {
    "info": {"label": "INFO", "color": CYAN},
    "success": {"label": "SUCCESS", "color": GREEN},
    "warning": {"label": "WARNING", "color": YELLOW},
    "error": {"label": "ERROR", "color": BRIGHT_CYAN},
    "critical": {"label": "CRITICAL", "color": CYAN},
}


def alert_banner(
    text: str,
    level: str = "info",
    width: int = 60,
    align: str = "left",
    border_style: str = "single",
) -> str:
    cfg = ALERT_STYLES.get(level, ALERT_STYLES["info"])
    styled_label = f"{BOLD}{cfg['color']}[ {cfg['label']} ]{RESET}"
    styled_text = f"{cfg['color']}{text}{RESET}"
    inner_w = width - 4
    s = BOX_STYLES.get(border_style, BOX_STYLES["single"])
    tl = f"{cfg['color']}{s['tl']}{RESET}"
    tr = f"{cfg['color']}{s['tr']}{RESET}"
    bl_ = f"{cfg['color']}{s['bl']}{RESET}"
    br = f"{cfg['color']}{s['br']}{RESET}"
    h = f"{cfg['color']}{s['h']}{RESET}"
    v = f"{cfg['color']}{s['v']}{RESET}"
    top = tl + h * (width - 2) + tr
    label_line = f"{v} {styled_label} {' ' * (inner_w - len(cfg['label']) - 4)} {v}"
    if align == "center":
        text_line = f"{v} {styled_text:^{inner_w}} {v}"
    elif align == "right":
        text_line = f"{v} {styled_text:>{inner_w}} {v}"
    else:
        text_line = f"{v} {styled_text:<{inner_w}} {v}"
    bot = bl_ + h * (width - 2) + br
    return f"{top}\n{label_line}\n{text_line}\n{bot}"


def progress_bar(
    pct: float = 50.0,
    width: int = 20,
    color: Optional[str] = None,
    fill_char: str = "█",
    empty_char: str = "░",
    show_pct: bool = True,
    label: Optional[str] = None,
) -> str:
    pct = max(0.0, min(100.0, pct))
    filled = int(round(pct / 100 * width))
    bar_color = color or ""
    fill = f"{bar_color}{fill_char * filled}{RESET}" if color else fill_char * filled
    empty = empty_char * (width - filled)
    bar = f"[{fill}{empty}]"
    if show_pct:
        pct_text = f" {pct:.0f}%"
        bar += pct_text
    if label:
        bar = f"{label} {bar}"
    return bar


def tag(
    text: str,
    color: str = BRIGHT_CYAN,
    invert: bool = False,
    bold: bool = True,
    bracket: str = "square",
) -> str:
    style_code = BOLD if bold else ""
    open_b, close_b = {"square": ("[", "]"), "round": ("(", ")"), "curly": ("{", "}"), "angle": ("<", ">"), "none": ("", "")}.get(bracket, ("[", "]"))
    if invert:
        tag_text = f"{open_b}{style_code}{color}{text}{RESET}{close_b}"
    else:
        tag_text = f"{open_b}{text}{close_b}"
        tag_text = f"{style_code}{color}{tag_text}{RESET}"
    return tag_text


def frame(
    art: str,
    box_style: str = "rounded",
    padding: int = 1,
    border_color: Optional[str] = None,
    title: Optional[str] = None,
    title_color: Optional[str] = None,
) -> str:
    return box(art, style=box_style, padding=padding, color=None, align="left", border_color=border_color, title=title, title_color=title_color)


def centered_banner(
    text: str,
    width: int = 50,
    fill: str = "─",
    color: str = CYAN,
    bold: bool = True,
    padding: int = 0,
) -> str:
    style_code = BOLD if bold else ""
    styled = f"{style_code}{color}{text}{RESET}"
    side = (width - len(text)) // 2
    line = f"{color}{fill * side}{RESET}{styled}{color}{fill * (width - side - len(text))}{RESET}"
    pad = "\n" * padding
    return pad + line + pad


def buddy_multi(
    project: str,
    animal_names: Optional[List[str]] = None,
    color: str = BRIGHT_CYAN,
    count: int = 2,
    spacing: int = 2,
    message: Optional[str] = None,
    message_color: Optional[str] = None,
) -> str:
    if animal_names:
        selected = [ANIMALS[n] for n in animal_names if n in ANIMALS]
        if not selected:
            selected = [random.choice(list(ANIMALS.values()))]
    else:
        names = ANIMAL_NAMES[:]
        random.shuffle(names)
        selected = [ANIMALS[n] for n in names[:min(count, len(names))]]
    lines_list = [a.split("\n") for a in selected]
    max_h = max(len(l) for l in lines_list)
    padded_arts = []
    for lines in lines_list:
        while len(lines) < max_h:
            lines.append("")
        padded_arts.append(lines)
    combined = []
    for i in range(max_h):
        row = (" " * spacing).join(lines[i] for lines in padded_arts)
        combined.append(row)
    art = "\n".join(combined)
    colored_art = color_art(art, color)
    styled_name = f"{BOLD}{color}{project}{RESET}"
    result = f"{colored_art}\n  {styled_name}"
    if message:
        msg_styled = _apply_color(f"  {message}", message_color or color)
        result += f"\n{msg_styled}"
    return result


# ──────────────────────────────────────────────
# Kaomoji — Japanese-style text emoticons
# ──────────────────────────────────────────────

KAOMOJI: Dict[str, List[str]] = {
    "happy": [
        "(◕‿◕)", "(^_^)", "(ᵔ◡ᵔ)", "(´▽`)", "(≧▽≦)", "ヽ(´▽`)/",
        "ヽ(>∀<☆)ノ", "٩(◕‿◕｡)۶", "(*´∀`*)", "(人•͈ᴗ•͈)", "(｡◕‿◕｡)",
        "(￣▽￣)ノ", "♪～(´ε｀ )", "₍ᵔ·͈༝·͈ᵔ₎", "(★^O^★)", "ヽ(・∀・)ﾉ",
        "(ﾉ◕ヮ◕)ﾉ", "ヽ(✿ﾟ▽ﾟ)ノ", "(*^▽^*)", "(´｡• ᵕ •｡`)",
    ],
    "sad": [
        "(T_T)", "(╥_╥)", "(｡•́︿•̀｡)", "(´；ω；`)", "(ノ_<。)",
        "(｡╯︵╰｡)", "(◞‸◟)", "( ˘ ³˘)♥", "( ˘⌣˘)♡",
        "(′︿‵｡)", "( ຈ ﹏ ຈ )", "(˃̣̣̥᷄⌓˂̣̣̥᷅)", "｡:ﾟ(;´∩`;)ﾟ:｡",
        "(⑅꒦ິ⌓꒦ີ)", "(´；д；`)", "(;﹏;)",
    ],
    "angry": [
        "(╬ Ò﹏Ó)", "ヽ(｀⌒´)ノ", "(╯°□°）╯︵ ┻━┻",
        "ლ(ಠ益ಠლ)", "( ͡⚆ ͜ʖ ͡⚆)", "(；一_一)",
        "(｀皿´)", "ψ(｀∇´)ψ", "(ノಠ ∩ಠ)ノ", "(╬▔皿▔)╯",
        "ヽ(｀Д´)ノ", "(ノ°□°)ノ⌒┻━┻", "ヽ(≧Д≦)ノ",
    ],
    "love": [
        "(♡˙︶˙♡)", "(♥‿♥)", "♡(˃͈ દ ˂͈ ˶)", "(⑅˘͈ ᵕ ˘͈)",
        "(｡♥‿♥｡)", "(˶ᵔ ᵕ ᵔ˶)", "❤(ӦｖӦ｡)", "💕(ˆ‿ˆ💕)",
        "°˖✧◝(⁰▿⁰)◜✧˖°", "(˘ʃƪ˘)", "( ˘ ³˘)♥",
        "♡(˶ˆ꒳ˆ˶)", "(ﾉ´ з `)ノ", "(◡ ω ◡)",
    ],
    "shrug": [
        "¯\\_(ツ)_/¯", "¯\\(°_o)/¯", "¯\\_(⊙︿⊙)_/¯",
        "┐(´ー｀)┌", "┑(￣▽￣)┍", "¯\\_(ᵔ̃ᵕᵔ̃)_/¯",
        "ヽ(ー_ー )ノ", "┐(￣∀￣)┌", "┐(´∀｀)┌",
        "ヽ(´ー｀)┌", "┐(˘_˘)┌",
    ],
    "cat": [
        "(=^・ω・^=)", "(=^‥^=)", "(^・ω・^)", "(=^･ω･^=)",
        "ᵒᴥᵒ#", "/ᐠ｡‸｡ᐟ\\", "ฅ^•ﻌ•^ฅ", "~ₒᴥₒ~",
        "／(=∵=)＼", "|ΦωΦ|", "⊹ₒᗐₒ⊹", "₍⸍⸌▶⍘◀⸍⸌₎",
        "(=^‥^=)", "₍^. .^₎⟆", "ᓚᘏᗢ",
    ],
    "dog": [
        "▼・ᴥ・▼", "U・ᴥ・U", "V•ᴥ•V", "￣ᴥ￣",
        "●ᴥ●", "(ᵔᴥᵔ)", "◖ᵔᴥᵔ◗", "ʕᵔᴥᵔʔ",
        "(ᵔᴥᵔ)", "U・ﻌ・U", "V・ᴥ・V",
    ],
    "bear": [
        "ʕ•ᴥ•ʔ", "ʕᵔᴥᵔʔ", "ʕ •`ᴥ•´ʔ", "ʕ̡̢̡ʘ̅͟͜͡ʘ̲̅ʔ̢̡̢",
        "ʕ·͡ᴥ·ʔ", "ʕ⊙ᴥ⊙ʔ", "ʕºᴥºʔ", "ʕ￫ᴥ￩ʔ",
        "ʕ·ᴥ·ʔ", "ʕ̡̢̡•̫•ʔ̢̡̢",
    ],
    "cute": [
        "(◕‿◕✿)", "(⁄ ⁄•⁄ω⁄•⁄ ⁄)", "(*/ω＼*)", "(〃∇〃)",
        "(｡>﹏<｡)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(づ｡◕‿‿◕｡)づ",
        "(๑˃̵ᴗ˂̵)و", "(っ˘ω˘ς)", "(｡•̀ᴗ-)✧",
        "(｀・ω・´)", "（>﹏<）", "(◕‿◕✿)",
    ],
    "surprise": [
        "Σ(°△°)", "(°ロ°)", "Σ(ﾟДﾟ；)", "∑(O_O;)",
        "(⊙_⊙)", "(°_°)", "ヾ(°∇°*)", "༼⁰o⁰；༽",
        "⊙﹏⊙", "(;′Д`)", "∑(°口°๑)", "(º Д º)",
        "ԅ(≖‿≖ԅ)", "(°◇°)",
    ],
    "sleep": [
        "(-_-)zzz", "(︶｡︶✽)", "(ᴗ˳ᴗ)", "zzzZ",
        "(´-ω-`)", "(ᵕ—ᴗ—)", "_(:3 」∠)_", "(_ _).oO",
        "( ˘ω˘ )", "(∪｡∪)｡｡zZ", "_(:3 」∠)_",
    ],
    "dance": [
        "ᕕ( ᐛ )ᕗ", "┏(＾0＾)┛", "♪┏(・o･)┛♪",
        "ヽ( ⌒o⌒)人(⌒-⌒ )ﾉ", "ᕕ(◎╱‿╱◎)ᕗ",
        "┏(^o^)┛", "┗(^o^ )┓", "┗(＾0＾)┓",
    ],
    "tableflip": [
        "(╯°□°）╯︵ ┻━┻", "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
        "(ノ°Д°）ノ︵ ┻━┻", "┻┻︵╰(‵□′)╯︵┻┻",
        "(╯‵□′)╯︵┻━┻", "┬─┬ ノ( ゜-゜ノ)",
    ],
    "party": [
        "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "ヽ(^◇^*)/", "✧*:･ﾟ✧ヽ(◕‿◕｡)ﾉ✧*:･ﾟ✧",
        "☆*:.｡.o(≧▽≦)o.｡.:*☆", "ヽ(★∀★)ﾉ", "₍ᐢ•ﻌ•ᐢ₎*･ﾟ✧",
    ],
    "greeting": [
        "( ´ ▽ ` )ﾉ", "ヽ(・∀・)ﾉ", "(ノ°▽°)ノ", "ヾ(＾∇＾)",
        "(*´∀`)ﾉ", "ヾ(•ω•`)o", "(￣▽￣)ノ", "ヽ(✧∀✧)ﾉ",
        "٩(◕‿◕)۶", "ヾ(´▽｀*)ゝ",
    ],
    "wave": [
        "ヽ(´▽｀)/", "ヾ(＾-＾)ノ", "( ´ ▽ ` )ﾉ", "ヽ(°□° )ﾉ",
        "( ^_^)／", "＼(^o^)／", "(・_・)ノ", "＼(°o°)／",
    ],
    "hug": [
        "(⊃｡•́‿•̀｡)⊃", "⊂(´• ω •`)⊃", "(づ￣ ³￣)づ",
        "⊂(◉‿◉)つ", "(っ˘ω˘ς)", "⊂(´･ω･`)⊃",
        "ヘ(^_^ヘ)", "(ノ^_^)ノ",
    ],
    "sorry": [
        "m(_ _)m", "(シ_ _)シ", "<(_ _)>", "人(_ _*)",
        "orz", "OTL", "m(＿ ＿)m", "（土下座）",
    ],
    "thank": [
        "ありがとう", "(人•͈ᴗ•͈)", "ヽ(^o^)丿", "ヾ(´▽｀*)ゝ",
        "(*´∀｀人)", "ヽ(´▽`)/♡", "（人´∀`*）",
    ],
    "excited": [
        "ヽ(>∀<☆)ノ", "ヽ(★∀★)ﾉ", "٩(˃̶͈̀௰˂̶͈́)و",
        "(ノ◕ヮ◕)ノ*:･ﾟ✧", "ヽ(^◇^*)/", "☆*:.｡.o(≧▽≦)o.｡.:*☆",
        "ヽ(｀▽´)ノ", "٩(●˙▿˙●)۶",
    ],
    "nervous": [
        "(；￣Д￣)", "(；一_一)", "(·᷄-·᷅)", "(,,•﹏•,,)",
        "(；´Д｀)", "(´-﹏-`；)", "(·•᷄‎ࡇ•᷅ )",
    ],
    "cool": [
        "(￣ω￣)", "(￣_,￣ )", "(¯▿¯)", "┌(・Σ・)┘",
        "ヽ(￣д￣)ノ", "(ー_ー)!!", "(◔_◔)",
    ],
    "run": [
        "ヽ(￣▿￣)ノ", "ε=ε=ε=ε=┏(゜ロ゜)┛", "┏(∵`)┛",
        "ヽ(●⁰౪⁰●)ﾉ", "ε=ε=ε=ε=ヽ(；▽；)ノ",
        "C= C= C= C=(o>ﾛ)o",
    ],
    "fight": [
        "(ง •̀_•́)ง", "(ง'̀-'́)ง", "ᕦ(ò_óˇ)ᕤ",
        "ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ", "ヽ(｀⌒´)ノ", "ᕦ( ⊡ 益 ⊡ )ᕤ",
        "ᕙ(⇀‸↼‶)ᕗ",
    ],
    "magic": [
        "☆.。.:*・°☆.。.:*・°", "ヽ( °◇°)ノ", "⊂( ｀▽´)⊃",
        "φ(゜▽゜*)♪", "⊂(ﾟヮﾟ)⊃", "☆ﾟ°˖*ヽ(˶￣▽￣˶)ヽ*˖°ﾟ☆",
    ],
    "food": [
        "(っ˘ڡ˘ς)", "(っ´ڡ`ς)", "ヽ(´～｀)ﾉ", "(っ˘~˘ς)",
        "(*´ڡ`*)", "(っ˘ω˘ς)", "༼ᵔ ͜ʖᵔ༽",
    ],
    "drink": [
        "ヽ(・∀・)ﾉ ┌∩┐", "(￣▽￣)ノ🍺", "ヽ(^o^)丿☕",
        "((((っ･◇･)っ", "(*＾▽＾)／☕",
    ],
    "music": [
        "♪♪(o*´ω｀*)o", "♫ヽ(゜∇゜ヽ)", "♪(┌・。・)┌",
        "♫♪.ılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılı.♫♪",
        "ヾ(´□｀*)ゝ♪", "♩♪♫♬ ヽ(^◇^*)/",
    ],
    "rain": [
        "☁️☁️☁️ (╥﹏╥)", "ヽ(；▽；)ノ☔", "༼ つ ◕_◕ ༽つ☔",
        "(´；ω；`)☔", "｡゜(｀Д´)゜｡☔",
    ],
    "star": [
        "☆彡", "★彡", "☆*:.｡.", "✧*:･ﾟ✧",
        "✦ ⋆ ｡ ﾟ", "🌠", "☆ﾟ°˖*",
    ],
    "flower": [
        "✿", "❀", "✿ﾟ❀", "🌸",
        "✿˘◡˘✿", "❀˘◡˘❀", "₊✿‧₊˚",
    ],
    "cold": [
        "(❁´◡`❁)", "🥶(≧▽≦)", "(((╹д╹;)))", "((ʅ‾́◡‾́)ʃ)",
        "༼ つ ◕‿◕ ༽つ❄️", "(☃️❄️)",
    ],
}

ALL_KAOMOJI: List[str] = [k for v in KAOMOJI.values() for k in v]


def kaomoji(category: Optional[str] = None) -> str:
    if category and category in KAOMOJI:
        return random.choice(KAOMOJI[category])
    return random.choice(ALL_KAOMOJI)


def kaomoji_list(category: Optional[str] = None) -> List[str]:
    if category and category in KAOMOJI:
        return KAOMOJI[category][:]
    return ALL_KAOMOJI[:]


def kaomoji_categories() -> List[str]:
    return list(KAOMOJI.keys())


# ──────────────────────────────────────────────
# ASCII art animals
# ──────────────────────────────────────────────

ANIMALS: Dict[str, str] = {
    "cat1": r"""
 |\__/,|   (`\
 |_ _  |.--.) )
 ( T   )     /
(((^_(((/(((_/
""".strip(),
    "cat2": r"""
  ｡ﾟ(ﾟ^㉨^ﾟ)ﾟ｡
""".strip(),
    "cat3": r"""
  ∧_∧
 (｡･ω･｡)
  ｜⊃／(
 ／⌒⌒
""".strip(),
    "cat_sleep": r"""
  |\      _,,,---,,_
  /,`.-'`'    -.  ;-;;,_
 |,4-  ) )-,_. ,\ (  `'-'
'---''(_/--'  `-'\_)
""".strip(),
    "cat_love": r"""
  |\__/,|
  |_ _  |
  ( @ @ )
   > ^ <
""".strip(),
    "dog1": r"""
     __
    /  \
 __|  |__
|o  o  o|
|  ___  |
 |_____|
""".strip(),
    "dog2": r"""
   __
o-'' )_____
 "--__/  |\_
    |  |  \)
    W  W
""".strip(),
    "dog_sleep": r"""
   __
  /  \
  |  |
  |__|
  /  \
( ' .')
  ″″
""".strip(),
    "bunny1": r"""
  (\
  ( -.-)
  o_(")(")
""".strip(),
    "bunny2": r"""
   (\
   (=';')
   (")(")
""".strip(),
    "bunny3": r"""
   /)/)
  ( . .)
  ( づ♡
""".strip(),
    "bear1": r"""
  ʕ•ᴥ•ʔ
""".strip(),
    "bear2": r"""
  ⊂(◉‿◉)つ
""".strip(),
    "penguin1": r"""
  ┏┓╋┏┓╋╋╋╋┏┓
  ┃┃╋┃┃╋╋╋╋┃┃
  ┃┗━┛┣━━┳━┛┃
  ┃┏━┓┃┏┓┃┏┓┃
  ┃┃╋┃┃┗┛┃┃┃┃
  ┗┛╋┗┻━━┻┛┗┛
""".strip(),
    "penguin2": (
        '  .---.\n'
        ' /     \\\n'
        ' |(. .)|\n'
        '  \\ v /\n'
        '  ("")'
    ),
    "penguin_dance": (
        '  .---.\n'
        ' / o o \\\n'
        ' |  ^  |\n'
        '  \\___/\n'
        '   | |\n'
        '  /   \\'
    ),
    "bird1": r"""
  ('v')
  (( ))
  ((""))
""".strip(),
    "bird2": r"""
  ___
 ('v')
 ((___))
  "   "
""".strip(),
    "fish1": r"""
  <°)))<{
""".strip(),
    "fish2": r"""
  ><((((*>>
""".strip(),
    "owl": r"""
  ,_,
 (O,O)
 (   )
 -"-"-
""".strip(),
    "fox": r"""
  /\_/\
 (^._.^)
  > ^ <
""".strip(),
    "pig": r"""
  (___)
  (o o)
  (   )
  ~~"`
""".strip(),
    "frog": r"""
   @..@
  (----)
  ( >__< )
  ^^ ~~ ^^
""".strip(),
    "koala": r"""
  .--.
 / () \
| \/\/ |
 \.__./
""".strip(),
    "panda": r"""
  ︵ ︵
 ( ▀▀ )
 (  ▐█)
 ︶ ︶
""".strip(),
    "turtle": r"""
  ___
 /   \
| O O |
 \___/
""".strip(),
    "monkey": (
        "  .-\"'-.\n"
        " /     \\\n"
        "| () ()|\n"
        " \\  ^  /\n"
        "  '\"\"\"'\n"
    ).strip(),
    "octopus": r"""
    ,---.
   / o o \
  |   O   |
  |  ===  |
   \_____/
""".strip(),
    "alien": r"""
  👽
""".strip(),
    "ghost": r"""
  .-.
 (X X)
 (   )
  '''
""".strip(),
    "robot": r"""
  .--.
 |o o|
 |_^_|
  '''
""".strip(),
    "lion": r"""
  ,_,
 (Y_Y)
 (   )
  ″″
""".strip(),
    "horse": r"""
  ,,-.
 /  .'|
 | ,' /|
 |/  / |
 \ /  /
  '--'
""".strip(),
    "cow": r"""
   (__)
   (oo)
   /  \/
  /    ||
 *-----\|
""".strip(),
    "sheep": r"""
      __
     /.~\\
    /. . \\
   /.' ' '\\
  / ' ' ' '\\
 /__________\\
  |       |
  |   ~   |
  |_______|
""".strip(),
    "elephant": r"""
     /\\
    /  \_
   /    \_____
  /           \\
  |  _     _   |
  | ( )   ( )  |
  |   -     -   |
  |_____________|
       |   |
       |   |
       U   U
""".strip(),
    "whale": r"""
     .-.
    |   \__
    |      \
    \       |
     `~~~~~~'
""".strip(),
    "dolphin": r"""
     ,-._
    /    \_
   |   _   \
   |  ( )   \
    \       /
     `-----'
""".strip(),
    "shark": r"""
   ,--.
  /  .'|
 / /  //
||   //
''   ||
    ,;'
   ''
""".strip(),
    "snake": r"""
   ___
  / _ \\
 / / \_\\
/ /_/___\\
\ \______/
 \_____/
""".strip(),
    "spider": r"""
  //_\\
 (o _ o)
  /   \
 //   \\\
""".strip(),
    "butterfly": r"""
  /\ /\
 (  .  )
  \__o_/
   /   \
  //   \\\
""".strip(),
    "parrot": r"""
   ,-.
  |O o|
  |   |
  '---'
""".strip(),
    "eagle": r"""
   /\
  /  \
 / __ \
( (__) )
 \____/
""".strip(),
    "wolf": r"""
      /\
     /  \
    /    \
   /  __  \
  /  (__)  \
 /__________\
    |    |
    |    |
   (  __  )
    \____/
""".strip(),
    "deer": r"""
   /\
  /  \
 /    \
/  __  \
| (__) |
 \____/
  |  |
  |  |
  U  U
""".strip(),
    "chicken": r"""
   __
  (  )
  /--\
 | () |
  \__/
""".strip(),
    "hamster": r"""
   .-.
  |o o|
  | w |
   '-'
""".strip(),
    "mouse": r"""
   .-.
  (o o)
  | W |
  '---'
     \\
""".strip(),
    "sloth": r"""
   .---.
  ( o o )
  /  |  \
 /   |   \
/    |    \
""".strip(),
    "dragon": r"""
   /\
  /  \
 /  __\
/  (__)\
\   \/
 \__/
""".strip(),
    "bat": r"""
   /\ /\
  ( . . )
  /  |  \
 // / \\ \\
""".strip(),
    "seal": r"""
   .-.
  (o o)
  | O |
  \___/
""".strip(),
    "octopus2": r"""
   .---.
  / o o \
 /   O   \
|   ---   |
 \_______/
""".strip(),
    "crab": r"""
   (  )
  (o o)
 /  |  \
/  / \  \
""".strip(),
    "dino": r"""
   .-.
  |o o|
  | W |
  |   |
 /_____\
""".strip(),
}

ANIMAL_NAMES: List[str] = list(ANIMALS.keys())


def animal(name: Optional[str] = None) -> str:
    if name and name in ANIMALS:
        return ANIMALS[name]
    return random.choice(list(ANIMALS.values()))


def animal_names() -> List[str]:
    return ANIMAL_NAMES[:]


# ──────────────────────────────────────────────
# Inline ASCII art (1-2 line emoticons / emoji)
# ──────────────────────────────────────────────

EMOJI: Dict[str, str] = {
    "smile": "☺︎",
    "heart": "♥",
    "heart_fill": "♡",
    "heart_bold": "❤",
    "heart_rotated": "💔",
    "heart_flower": "❦",
    "star": "★",
    "star_outline": "☆",
    "star_filled": "✦",
    "star_sparkle": "✧",
    "music": "♫",
    "music_double": "♫♪",
    "music_note": "♪",
    "music_eighth": "♩",
    "check": "✓",
    "check_heavy": "✔",
    "cross": "✗",
    "cross_heavy": "✘",
    "cross_mark": "✕",
    "sun": "☀",
    "moon": "☽",
    "moon_fill": "☾",
    "cloud": "☁",
    "umbrella": "☂",
    "snowman": "☃",
    "skull": "☠",
    "peace": "☮",
    "yin_yang": "☯",
    "warning": "⚠",
    "radiation": "☢",
    "biohazard": "☣",
    "spade": "♠",
    "club": "♣",
    "diamond": "♦",
    "heart_suit": "♥",
    "arrow_up": "↑",
    "arrow_down": "↓",
    "arrow_left": "←",
    "arrow_right": "→",
    "arrow_updown": "↕",
    "arrow_up_strict": "⇑",
    "arrow_down_strict": "⇓",
    "arrow_left_strict": "⇐",
    "arrow_right_strict": "⇒",
    "arrow_updown_double": "⇕",
    "lightning": "⚡",
    "gear": "⚙",
    "crown": "♔",
    "anchor": "⚓",
    "scissors": "✂",
    "pencil": "✎",
    "flower": "✿",
    "flower_outline": "❀",
    "snowflake": "❄",
    "snowflake_heavy": "❅",
    "phone": "☏",
    "envelope": "✉",
    "coffee": "☕",
    "target": "◎",
    "infinity": "∞",
    "male": "♂",
    "female": "♀",
    "recycle": "♲",
    "wheelchair": "♿",
    "zodiac_aries": "♈",
    "zodiac_taurus": "♉",
    "zodiac_gemini": "♊",
    "zodiac_cancer": "♋",
    "zodiac_leo": "♌",
    "zodiac_virgo": "♍",
    "zodiac_libra": "♎",
    "zodiac_scorpio": "♏",
    "zodiac_sagittarius": "♐",
    "zodiac_capricorn": "♑",
    "zodiac_aquarius": "♒",
    "zodiac_pisces": "♓",
    "chess_king": "♚",
    "chess_queen": "♛",
    "chess_rook": "♜",
    "chess_bishop": "♝",
    "chess_knight": "♞",
    "chess_pawn": "♟",
    "math_plus": "+",
    "math_minus": "−",
    "math_times": "×",
    "math_divide": "÷",
    "math_sqrt": "√",
    "math_infinity": "∞",
    "math_integral": "∫",
    "math_sum": "∑",
    "math_product": "∏",
    "degree": "°",
    "copyright": "©",
    "registered": "®",
    "trademark": "™",
    "euro": "€",
    "pound": "£",
    "yen": "¥",
    "cent": "¢",
    "dollar": "$",
    "pilcrow": "¶",
    "section": "§",
    "dagger": "†",
    "double_dagger": "‡",
    "bullet": "•",
    "lozenge": "◊",
    "circle": "○",
    "circle_fill": "●",
    "square": "□",
    "square_fill": "■",
    "triangle_up": "▲",
    "triangle_down": "▼",
    "triangle_left": "◀",
    "triangle_right": "▶",
    "diamond_shape": "◆",
    "circle_dot": "⊙",
    "circle_cross": "⊗",
    "smiley": "☺",
    "frown": "☹",
    "check_box": "☑",
    "radio_on": "◉",
    "radio_off": "◎",
}

ALL_EMOJI_NAMES: List[str] = list(EMOJI.keys())


def emoji(name: Optional[str] = None) -> str:
    if name and name in EMOJI:
        return EMOJI[name]
    return random.choice(list(EMOJI.values()))


def emoji_names() -> List[str]:
    return ALL_EMOJI_NAMES[:]


# ──────────────────────────────────────────────
# Buddy / Mascot — combine animal + project name
# ──────────────────────────────────────────────

def buddy(
    project: str,
    animal_name: Optional[str] = None,
    color: str = BRIGHT_CYAN,
    align: str = "left",
    message: Optional[str] = None,
    message_color: Optional[str] = None,
    show_name: bool = True,
) -> str:
    art = animal(animal_name)
    colored_art = color_art(art, color)
    result = colored_art
    if show_name:
        styled_name = f"{BOLD}{color}{project}{RESET}"
        result += f"\n  {styled_name}"
    if message:
        msg_styled = _apply_color(f"  {message}", message_color or color)
        result += f"\n{msg_styled}"
    if align == "center":
        lines = result.split("\n")
        max_w = max(len(l) for l in lines)
        result = "\n".join(l.center(max_w) for l in lines)
    elif align == "right":
        lines = result.split("\n")
        max_w = max(len(l) for l in lines)
        result = "\n".join(l.rjust(max_w) for l in lines)
    return result


def buddy_box(
    project: str,
    tagline: Optional[str] = None,
    animal_name: Optional[str] = None,
    color: str = BRIGHT_CYAN,
    box_style: str = "rounded",
    align: str = "left",
    padding: int = 0,
    border_color: Optional[str] = None,
    message: Optional[str] = None,
    message_color: Optional[str] = None,
) -> str:
    art = animal(animal_name)
    colored_art = color_art(art, color)
    styled_name = f"{BOLD}{color}{project}{RESET}"
    content = f"{colored_art}\n  {styled_name}"
    if tagline:
        tag_styled = _apply_color(f"  {tagline}", color)
        content += f"\n{tag_styled}"
    if message:
        msg_styled = _apply_color(f"  {message}", message_color or color)
        content += f"\n{msg_styled}"
    return box(content, style=box_style, title=project, align=align, padding=padding, border_color=border_color, title_color=color)
