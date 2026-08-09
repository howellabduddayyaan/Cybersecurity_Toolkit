# ====================
# === Table format ===
# ====================

def print_table(title, data):

    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)

    for key, value in data.items():
        print(f"{key:<20}: {value}")

    print("=" * 50)
    
# _________________________________________________________________________________________________