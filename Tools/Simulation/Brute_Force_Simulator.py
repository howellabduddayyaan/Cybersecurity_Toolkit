# ==============================
# === Brute Force Simulator ===
# ==============================

import itertools
import string
import time

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

def brute_force(target, characters):

    attempts = 0

    start_time = time.time()

    for length in range(1, len(target) + 1):

        combinations = itertools.product(characters,repeat=length)

        for combination in combinations:

            attempt = "".join(combination)

            attempts += 1

            print(
                f"\rAttempts: {attempts:<8} "
                f"Trying: {attempt:<10}",
                end=""
            )

            if attempt == target:

                end_time = time.time()

                print()

                return {
                    "Result": "Password Found",
                    "Password": attempt,
                    "Attempts": attempts,
                    "Time": f"{end_time - start_time:.2f} seconds"
                }

    print()

    return {
        "Result": "Password Not Found",
        "Password": "N/A",
        "Attempts": attempts,
        "Time": f"{time.time() - start_time:.2f} seconds"
    }


# _________________________________________________________________________________________________
