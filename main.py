from time import sleep

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
from typefx.colors import (
    AMBER,
    AQUA,
    BIM,
    BOLD,
    BRIGHT_CYAN,
    BRIGHT_GREEN,
    BRIGHT_MAGENTA,
    BRIGHT_RED,
    BRIGHT_WHITE,
    BRIGHT_YELLOW,
    CERULEAN,
    CORAL,
    CRIMSON,
    CYAN,
    GREEN,
    LILAC,
    MINT,
    OVERLINE,
    PINK,
    PLUM,
    PURPLE,
    RESET,
    SLATE,
    TOMATO,
    UNDERLINE,
    colorize,
)
from typefx.styles import (
    ACCENT,
    BANNER,
    CAPTION,
    CODE,
    CRITICAL,
    DANGER,
    DEBUG,
    DIM,
    EMPHASIS,
    ERROR,
    GHOST,
    HEADING,
    HIGHLIGHT,
    HINT,
    IMPORTANT,
    INFO,
    KEYWORD,
    LABEL,
    LINK,
    LOG,
    META,
    MUTED,
    NEON,
    NOTE,
    PRIMARY,
    PUNCH,
    QUOTE,
    SECONDARY,
    STRIKETHROUGH,
    SUBHEADING,
    SUCCESS,
    TAG,
    TIP,
    TITLE,
    TRACE,
    VERBOSE,
    WARNING,
    apply_style,
)
from typefx.writers import GradientWriter, RainbowWriter, TypeWriter


def demo_colors():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ New Colors ━━━{RESET}")
    for name, code in [
        ("AMBER", AMBER),
        ("CERULEAN", CERULEAN),
        ("CORAL", CORAL),
        ("CRIMSON", CRIMSON),
        ("LILAC", LILAC),
        ("MINT", MINT),
        ("PINK", PINK),
        ("PLUM", PLUM),
        ("PURPLE", PURPLE),
        ("SLATE", SLATE),
        ("TOMATO", TOMATO),
    ]:
        sample = colorize(f" {name:12}", code, BOLD)
        print(f"  {sample}")


def demo_styles():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Style Presets ━━━{RESET}")
    styles = [
        ("ERROR", ERROR),
        ("SUCCESS", SUCCESS),
        ("WARNING", WARNING),
        ("INFO", INFO),
        ("TIP", TIP),
        ("HINT", HINT),
        ("DANGER", DANGER),
        ("CRITICAL", CRITICAL),
        ("IMPORTANT", IMPORTANT),
        ("NOTE", NOTE),
        ("DEBUG", DEBUG),
        ("TRACE", TRACE),
        ("LOG", LOG),
        ("VERBOSE", VERBOSE),
        ("PRIMARY", PRIMARY),
        ("SECONDARY", SECONDARY),
        ("ACCENT", ACCENT),
        ("MUTED", MUTED),
        ("GHOST", GHOST),
        ("DIM", DIM),
        ("PUNCH", PUNCH),
        ("EMPHASIS", EMPHASIS),
        ("BANNER", BANNER),
        ("TITLE", TITLE),
        ("HEADING", HEADING),
        ("SUBHEADING", SUBHEADING),
        ("CODE", CODE),
        ("KEYWORD", KEYWORD),
        ("LINK", LINK),
        ("QUOTE", QUOTE),
        ("CAPTION", CAPTION),
        ("LABEL", LABEL),
        ("TAG", TAG),
        ("HIGHLIGHT", HIGHLIGHT),
        ("STRIKETHROUGH", STRIKETHROUGH),
        ("NEON", NEON),
        ("META", META),
    ]
    for name, style in styles:
        print(f"  {apply_style(f'{name:18}', style)}")


def demo_writers():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Writers ━━━{RESET}")
    TypeWriter("TypeWriter", delay=0.02, **SUCCESS)
    sleep(0.1)
    RainbowWriter("RainbowWriter", delay=0.02)
    sleep(0.1)
    GradientWriter(
        "GradientWriter",
        delay=0.02,
        start_color=BRIGHT_CYAN,
        end_color=BRIGHT_MAGENTA,
    )


def demo_apply_style():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ apply_style ━━━{RESET}")
    styled = apply_style("Bold & Underlined", {"style": (BOLD, UNDERLINE)})
    aqua = apply_style("Aqua text", {"color": AQUA})
    combo = apply_style("Custom Combo", {"color": BRIGHT_YELLOW, "style": (BOLD, OVERLINE)})
    print(f"  {styled}")
    print(f"  {aqua}")
    print(f"  {combo}")


def demo_banners():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Banners ━━━{RESET}")

    print(f"\n{BIM}project_banner:{RESET}")
    print(project_banner("PyTypeFx", tagline="Terminal Text Effects", version="2.0.1"))

    print(f"\n{BIM}box (single):{RESET}")
    print(box("Hello from PyTypeFx!", style="single"))

    print(f"\n{BIM}box (double, titled):{RESET}")
    print(box("Content here", style="double", title="Output"))

    print(f"\n{BIM}box (rounded):{RESET}")
    print(box("Rounded Box", style="rounded"))

    print(f"\n{BIM}banner_block:{RESET}")
    print(banner_block("PyTypeFx"))

    print(f"\n{BIM}banner_arrow:{RESET}")
    print(banner_arrow("Next Step"))

    print(f"\n{BIM}banner_dash:{RESET}")
    print(banner_dash("Feature Demo"))

    print(f"\n{BIM}section_header:{RESET}")
    print(section_header("Installation", color=CYAN))

    print(f"\n{BIM}divider:{RESET}")
    print(divider(char="=", length=30))
    print(divider(label="END", length=30))


def main():
    print(f"{BOLD}{BRIGHT_CYAN}{OVERLINE}  PyTypeFx Demo v2.0.1  {RESET}")
    print(f"  {colorize('Expanded colors, banners & more', BRIGHT_GREEN, BIM)}")

    demo_banners()
    demo_colors()
    demo_styles()
    demo_writers()
    demo_apply_style()

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Done ━━━{RESET}\n")


if __name__ == "__main__":
    main()
