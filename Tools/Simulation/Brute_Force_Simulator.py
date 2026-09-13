# ==============================
# === Brute Force Simulator ===
# ==============================

import itertools
import string
import time

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# --- Apply Brute Force ---

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

def main():

    show_banner("Brute Force Simulator")

    print("\nThis is my educational simulator")

    print("Use short test passwords to keep the simulation fast\n")

    target = input("Enter target password: ").strip()

    if not target:

        print("\nPlease enter a target password")

        pause()

        return

# --- Character Set Menu ---

    print("""
Choose character set:

1. Lowercase letters
2. Lowercase + numbers
3. Letters + numbers
""")

    choice = input("Choose an option: ").strip()

# --- Select Character Set ---

    if choice == "1":

        characters = string.ascii_lowercase

        character_set = "Lowercase letters"

    elif choice == "2":

        characters = (string.ascii_lowercase + string.digits)

        character_set = "Lowercase + numbers"

    elif choice == "3":

        characters = (string.ascii_letters + string.digits)

        character_set = "Letters + numbers"

    else:

        print("\nInvalid option")

        pause()

        return

# --- Simulation Information ---

    print_section(
        "Simulation Information",
        {
            "Target Length": len(target),
            "Character Set": character_set
        }
    )

    print("\nStarting simulation...\n")

# --- Run Simulation ---

    result = brute_force(target,characters)

    print_section("Simulation Results",result)

    analysis_complete = "Analysis Complete"
    print_analysis_complete(analysis_complete)

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________