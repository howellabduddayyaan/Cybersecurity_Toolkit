# ======================
# === Menu Utilities ===
# ======================

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def line():
    print("-" * 60)
    
# _________________________________________________________________________________________________