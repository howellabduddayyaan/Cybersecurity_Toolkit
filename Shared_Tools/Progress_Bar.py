# ====================
# === Progress Bar ===
# ====================

import sys

def progress(current, total):

    percent = int((current / total) * 100)

    bar_length = 30

    filled = int(bar_length * current // total)

    bar = "█" * filled + "-" * (bar_length - filled)

    sys.stdout.write(
        f"\r|{bar}| {percent}% ({current}/{total})"
    )

    sys.stdout.flush()

    if current == total:
        print()
        
# _________________________________________________________________________________________________