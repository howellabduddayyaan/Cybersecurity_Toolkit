# ====================
# === Log Analyzer ===
# ====================

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

def analyze_log(filename):

    try:

        with open(filename, "r") as file:
            lines = file.readlines()

    except FileNotFoundError:

        print("\nError: File not found :(")

        return

# _________________________________________________________________________________________________

    total_lines = len(lines)

    info = 0
    warnings = 0
    errors = 0
    failed_logins = 0


    for line in lines:

        line = line.upper()

        if "INFO" in line:
            info += 1

        if "WARNING" in line:
            warnings += 1

        if "ERROR" in line:
            errors += 1

        if "FAILED LOGIN" in line:
            failed_logins += 1

# _________________________________________________________________________________________________

