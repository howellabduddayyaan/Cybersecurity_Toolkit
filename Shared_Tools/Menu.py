# ====================
# === Display Menu ===
# ====================

def show_menu(title, options):

    print(f"\n=== {title} ===\n")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    print("0. | Back")
    
# _________________________________________________________________________________________________