# ====================
# === Table format ===
# ====================

def print_section(title, data):

    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80)

    for key, value in data.items():
        print(f"{key:<20}: {value}")

    print()
    
# _________________________________________________________________________________________________

def print_analysis_complete(analysis_complete):

    print("=" * 80)
    print(analysis_complete.center(80))
    print("=" * 80)
    
# _________________________________________________________________________________________________