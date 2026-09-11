# ====================
# === Table format ===
# ====================

TABLE_WIDTH = 80

def print_section(title, data):

    print("\n" + "=" * TABLE_WIDTH )
    print(title.center(TABLE_WIDTH ))
    print("=" * TABLE_WIDTH )

    for key, value in data.items():
        print(f"{key:<20}: {value}")

    print()


def print_analysis_complete(analysis_complete):

    print("=" * TABLE_WIDTH )
    print(analysis_complete.center(TABLE_WIDTH ))
    print("=" * TABLE_WIDTH )
    
# _________________________________________________________________________________________________