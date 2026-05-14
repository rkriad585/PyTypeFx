from time import sleep

from typefx.banners import (
    alert_banner,
    animal,
    banner_arrow,
    banner_block,
    banner_dash,
    box,
    buddy,
    buddy_box,
    buddy_multi,
    centered_banner,
    color_art,
    divider,
    emoji,
    frame,
    hero_banner,
    kaomoji,
    progress_bar,
    project_banner,
    rule,
    section_header,
    tag,
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
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Project Banner ━━━{RESET}")
    print(project_banner("PyTypeFx", tagline="Terminal Text Effects", version="2.0.1"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Boxes ━━━{RESET}")
    print(box("Hello from PyTypeFx!", style="single"))
    print(box("Content here", style="double", title="Output"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Customizable Box ━━━{RESET}")
    print(box("Customized", color=BRIGHT_CYAN, align="center", padding=1, width=30, title="Demo"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Hero Banner ━━━{RESET}")
    print(hero_banner("PyTypeFx v2.0.1"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Alerts ━━━{RESET}")
    print(alert_banner("System is running smoothly", level="success", width=50))
    print(alert_banner("Resource usage is high", level="warning", width=50))
    print(alert_banner("Connection lost", level="critical", width=50))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Progress Bars ━━━{RESET}")
    print(progress_bar(25, width=20, label="Download"))
    print(progress_bar(50, width=20, label="Processing"))
    print(progress_bar(100, width=20, label="Complete"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Tags ━━━{RESET}")
    for name in ["INFO", "WARN", "ERROR", "DEBUG", "DONE"]:
        print(f"  {tag(name, bracket='square')}")

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Banner Styles ━━━{RESET}")
    print(banner_block("PyTypeFx"))
    print(banner_arrow("Next Step"))
    print(banner_dash("Feature Demo"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Divider & Rules ━━━{RESET}")
    print(divider(length=40, label="Section", color=CYAN))
    print(rule(length=40, char="=", color=CYAN))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Centered Banner ━━━{RESET}")
    print(centered_banner("★ PyTypeFx ★", width=50, color=BRIGHT_CYAN, bold=True))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Frame Around Art ━━━{RESET}")
    print(frame("  Hello\n  World", box_style="double"))


def demo_kaomoji():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Kaomoji ━━━{RESET}")
    cats = ["happy", "sad", "angry", "love", "shrug", "cat", "dog", "bear", "cute", "party"]
    for cat in cats:
        k = kaomoji(cat)
        print(f"  {cat:10} {k}")

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ New Kaomoji ━━━{RESET}")
    for cat in ["greeting", "hug", "sorry", "excited", "magic", "food", "fight", "run"]:
        k = kaomoji(cat)
        print(f"  {cat:10} {k}")


def demo_animals():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Animals ━━━{RESET}")
    for name in ["cat1", "dog1", "bunny1", "bear1", "penguin2", "bird1", "fish1", "owl", "fox", "pig", "frog", "turtle", "monkey"]:
        print(f"  {name:12}")
        art = animal(name)
        for line in art.split("\n"):
            print(f"    {line}")
        print()

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ New Animals ━━━{RESET}")
    for name in ["lion", "horse", "cow", "sheep", "elephant", "whale", "dolphin", "snake", "butterfly", "wolf", "dragon", "bat", "seal", "dino"]:
        print(f"  {name:12}")
        art = animal(name)
        for line in art.split("\n"):
            print(f"    {line}")
        print()


def demo_buddy():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Buddy / Mascot ━━━{RESET}")
    print(buddy("PyTypeFx", animal_name="cat1", color=BRIGHT_CYAN))
    print()
    print(buddy("PyTypeFx", animal_name="bear1", color=BRIGHT_GREEN))
    print()
    print(buddy_box("PyTypeFx", tagline="Terminal Text Effects", animal_name="fox"))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Buddy Multi ━━━{RESET}")
    print(buddy_multi("PyTypeFx", animal_names=["cat1", "dog1", "fox"], color=BRIGHT_CYAN))

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Buddy with Message ━━━{RESET}")
    print(buddy("PyTypeFx", animal_name="penguin2", color=BRIGHT_CYAN, message="Making terminals beautiful!"))


def demo_emoji():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Emoji ━━━{RESET}")
    for name in ["heart", "star", "smile", "sun", "moon", "music", "check", "warning", "lightning", "flower", "snowflake", "coffee"]:
        e = emoji(name)
        print(f"  {name:12} {e}")

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ New Emoji ━━━{RESET}")
    for name in ["heart_bold", "star_sparkle", "check_heavy", "arrow_right_strict", "chess_king", "zodiac_aries", "degree", "infinity", "bullet", "radio_on"]:
        e = emoji(name)
        print(f"  {name:20} {e}")


def main():
    print(f"{BOLD}{BRIGHT_CYAN}{OVERLINE}  PyTypeFx Demo v2.0.1  {RESET}")
    print(f"  {colorize('Banners, animals, kaomoji & more', BRIGHT_GREEN, BIM)}")

    demo_banners()
    demo_kaomoji()
    demo_animals()
    demo_buddy()
    demo_emoji()
    demo_colors()
    demo_styles()
    demo_writers()
    demo_apply_style()

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Done ━━━{RESET}\n")


if __name__ == "__main__":
    main()
