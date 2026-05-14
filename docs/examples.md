# TypeFx Examples

## Banner Examples

### 1. Project Startup Banner

```python
from typefx import project_banner, hero_banner, alert_banner, divider, progress_bar
from typefx.colors import BRIGHT_CYAN, CYAN, GREEN

print(hero_banner("MyApp Server v2.0", color=BRIGHT_CYAN, width=60))
print(alert_banner("Server starting on port 8080", level="info", width=60))
print(divider(length=60, color=CYAN))
print(progress_bar(100, width=30, label="Initialized", color=GREEN))
```

### 2. Customizable Box Layouts

```python
from typefx import box
from typefx.colors import BRIGHT_CYAN, CYAN, GREEN, YELLOW

# Minimal
print(box("Hello"))

# With title
print(box("Content", style="double", title="Output"))

# Fully customized
print(box(
    "Customized Content",
    style="double",
    title="Output",
    color=BRIGHT_CYAN,
    align="center",
    padding=1,
    width=40,
))
```

### 3. Alert System

```python
from typefx import alert_banner

levels = ["info", "success", "warning", "error", "critical"]
messages = [
    "Server started on port 8080",
    "Deployment completed successfully",
    "Disk usage at 85%",
    "Connection to database lost",
    "System shutting down immediately",
]
for level, msg in zip(levels, messages):
    print(alert_banner(msg, level=level, width=60))
```

### 4. Progress Bars

```python
from typefx import progress_bar
from typefx.colors import GREEN, YELLOW, RED
import time

def simulate_install():
    stages = [
        ("Installing dependencies...", 10, YELLOW),
        ("Building modules...", 40, YELLOW),
        ("Configuring settings...", 65, GREEN),
        ("Optimizing...", 85, GREEN),
        ("Complete!", 100, GREEN),
    ]
    for label, pct, color in stages:
        print(progress_bar(pct, width=25, label=label, color=color))
        time.sleep(0.5)

simulate_install()
```

### 5. Tags / Badges for Logging

```python
from typefx import tag
from typefx.colors import BRIGHT_CYAN, GREEN, YELLOW, RED

def log_info(msg):
    print(f"{tag('INFO', color=BRIGHT_CYAN)} {msg}")

def log_success(msg):
    print(f"{tag('DONE', color=GREEN, bracket='round')} {msg}")

def log_warn(msg):
    print(f"{tag('WARN', color=YELLOW, bracket='curly')} {msg}")

def log_error(msg):
    print(f"{tag('FAIL', color=RED, bracket='angle')} {msg}")

log_info("Loading config...")
log_success("Config loaded")
log_warn("Deprecated setting found")
log_error("Missing database driver")
```

### 6. Divider Styles

```python
from typefx import divider, rule
from typefx.colors import CYAN, GREEN, YELLOW, BRIGHT_CYAN

print(divider(label="Section 1", color=CYAN, align="center"))
print(divider(label="Start", color=GREEN, align="left"))
print(divider(label="End", color=YELLOW, align="right"))
print(rule(char="=", color=BRIGHT_CYAN, length=40))
```

### 7. Buddy Mascot

```python
from typefx import buddy, buddy_box, buddy_multi
from typefx.colors import BRIGHT_CYAN, BRIGHT_GREEN, BRIGHT_MAGENTA

# Simple buddy
print(buddy("MyApp", animal_name="cat1", color=BRIGHT_CYAN))

# With message
print(buddy("MyApp", animal_name="penguin2", color=BRIGHT_CYAN,
            message="Making terminals beautiful!"))

# Boxed
print(buddy_box("MyApp", tagline="v2.0", animal_name="fox",
                color=BRIGHT_MAGENTA, box_style="double"))

# Multiple animals
print(buddy_multi("MyApp", animal_names=["cat1", "fox", "penguin2"],
                  color=BRIGHT_CYAN, spacing=4))
```

### 8. All Animals Gallery

```python
from typefx import animal, animal_names

for name in animal_names():
    print(f"\n--- {name} ---")
    print(animal(name))
```

### 9. Kaomoji Explorer

```python
from typefx import kaomoji, kaomoji_categories

for cat in kaomoji_categories():
    print(f"{cat:12} {kaomoji(cat)}")
```

### 10. Section Headers

```python
from typefx import section_header
from typefx.colors import CYAN, BRIGHT_CYAN

print(section_header("Left Aligned", color=CYAN))
print(section_header("Centered", align="center", color=BRIGHT_CYAN))
print(section_header("Right Aligned", align="right", color=CYAN))
```

### 11. Color Art

```python
from typefx import color_art, animal
from typefx.colors import BRIGHT_CYAN, GREEN, BRIGHT_MAGENTA, BG_BLUE

dragon = animal("dragon")
print(color_art(dragon, BRIGHT_CYAN))
print(color_art(dragon, BRIGHT_MAGENTA, align="center", width=30))
```

### 12. Frame Around Output

```python
from typefx import frame, animal

print(frame(animal("dragon"), box_style="double", title="Dragon"))
print(frame("  Hello\n  World", box_style="rounded", padding=2))
```

### 13. Centered Banners

```python
from typefx import centered_banner
from typefx.colors import BRIGHT_CYAN, CYAN, GREEN

print(centered_banner("★ Welcome ★", width=50, color=BRIGHT_CYAN, bold=True))
print(centered_banner("--- Section ---", width=40, color=CYAN, fill="~"))
print(centered_banner(">>> DONE <<<", width=30, color=GREEN, fill="="))
```

### 14. Combining Everything — Full CLI Output

```python
from typefx import *
from typefx.colors import *

def startup_banner(app_name, version, port):
    print(hero_banner(f"{app_name} v{version}", color=BRIGHT_CYAN, width=60))
    print(alert_banner(f"Server starting on port {port}", level="info", width=60))
    print(divider(length=60, color=CYAN, label="Modules", align="center"))
    print(progress_bar(20, width=25, label="Loading config", color=YELLOW))
    print(progress_bar(60, width=25, label="Initializing", color=YELLOW))
    print(progress_bar(100, width=25, label="Ready", color=GREEN))
    print()
    print(centered_banner("★ System Online ★", width=50, color=GREEN))
    print()
    print(buddy(app_name, animal_name="dragon", color=BRIGHT_CYAN,
                message="Ready to serve!"))

startup_banner("MyAPI", "2.0", 8080)
```

### 15. Emoji Symbols Reference

```python
from typefx import emoji, emoji_names

print("\\n=== Hearts ===")
for name in emoji_names():
    if "heart" in name:
        print(f"  {name:20} {emoji(name)}")

print("\\n=== Arrows ===")
for name in emoji_names():
    if "arrow" in name:
        print(f"  {name:20} {emoji(name)}")

print("\\n=== Zodiac ===")
for name in emoji_names():
    if "zodiac" in name:
        print(f"  {name:20} {emoji(name)}")
```
