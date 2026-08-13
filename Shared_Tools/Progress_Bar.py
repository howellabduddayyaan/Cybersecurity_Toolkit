# ====================
# === Progress Bar ===
# ====================

import sys

def progress(current, total,label="Scanning"):

    percent = int((current / total) * 100)

    bar_length = 30

    filled = int(bar_length * current // total)

    bar = "█" * filled + "-" * (bar_length - filled)

    sys.stdout.write(
        f"\r{label}:|{bar}|" 
        f"{percent}% "
        f"({current}/{total})"
    )

    sys.stdout.flush()

    if current == total:
        print()
        
# _________________________________________________________________________________________________