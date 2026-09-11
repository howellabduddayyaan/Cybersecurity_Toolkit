# =================================
# === Password Strength Checker ===
# =================================

import string

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause


def check_password_strength(password):

    score = 0
    checks = []

# --- Length Check ---

    if len(password) >= 8:

        score += 1
        checks.append("At least 8 characters: PASS")

    else:

        checks.append("At least 8 characters: FAIL")

# --- Uppercase Check ---

    if any(char.isupper() for char in password):

        score += 1
        checks.append("Contains uppercase letter: PASS")

    else:

        checks.append("Contains uppercase letter: FAIL")

# --- Lowercase Check ---

    if any(char.islower() for char in password):

        score += 1
        checks.append("Contains lowercase letter: PASS")

    else:

        checks.append("Contains lowercase letter: FAIL")

# --- Number Check ---

    if any(char.isdigit() for char in password):

        score += 1
        checks.append("Contains number: PASS")

    else:

        checks.append("Contains number: FAIL")

# --- Special Character Check ---

    if any(char in string.punctuation for char in password):

        score += 1
        checks.append("Contains special character: PASS")

    else:

        checks.append("Contains special character: FAIL")

# --- Password Length Check ---

    if len(password) >= 12:

        score += 1
        checks.append("At least 12 characters: PASS")

    else:

        checks.append("At least 12 characters: FAIL")

# --- Determine Strength ---

    if score <= 2:

        strength = "WEAK"

    elif score <= 4:

        strength = "MEDIUM"

    elif score == 5:

        strength = "STRONG"

    else:

        strength = "VERY STRONG"

    return score, strength, checks


# _________________________________________________________________________________________________

def main():

    show_banner("Password Strength Checker")

    password = input("\nEnter password to check: ")

    if not password:

        print("\nPassword cannot be empty")

        pause()

        return

# --- Password Analysis ---

    score, strength, checks = (check_password_strength(password))

    print_section(
        "Password Analysis",
        {
            "Password Length": len(password),
            "Score": f"{score}/6",
            "Strength": strength
        }
    )

# --- Security Checks ---

    print("--- Security Checks ---\n")

    print(f"{'Check':<40}Result")

    print("-" * 55)

    for check in checks:

        parts = check.rsplit(": ",1)

        print(
            f"{parts[0]:<40}"
            f"{parts[1]}"
        )

# --- Recommendation ---

    print()

    if strength == "WEAK":

        print(
            "Recommendation: Use a longer password "
            "with different character types"
        )

    elif strength == "MEDIUM":

        print(
            "Recommendation: Add more characters "
            "and increase the password length"
        )

    elif strength == "STRONG":

        print("Recommendation: Good password strength")

    else:

        print("Recommendation: Excellent password strength")

    analysis_complete = "Analysis Complete"
    
    print_analysis_complete(analysis_complete)

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________