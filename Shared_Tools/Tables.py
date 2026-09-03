# ====================
# === Table format ===
# ====================

def print_section(title, data):

    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)

    for key, value in data.items():
        print(f"{key:<20}: {value}")

    print()
    
# _________________________________________________________________________________________________

def print_analysis_complete(analysis_complete):

    print("=" * 70)
    print(analysis_complete.center(70))
    print("=" * 70)
    
# _________________________________________________________________________________________________