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

# _________________________________________________________________________________________________
    
# ------
# Length
# ------

    if len(password) >= 8:

        score += 1
        checks.append("At least 8 characters: PASS")

    else:

        checks.append("At least 8 characters: FAIL")

# _________________________________________________________________________________________________

# ---------
# Uppercase
# ---------

    if any(char.isupper() for char in password):

        score += 1
        checks.append("Contains uppercase letter: PASS")

    else:

        checks.append("Contains uppercase letter: FAIL")

# _________________________________________________________________________________________________

# ---------
# Lowercase
# ---------

    if any(char.islower() for char in password):

        score += 1
        checks.append("Contains lowercase letter: PASS")

    else:

        checks.append("Contains lowercase letter: FAIL")

# _________________________________________________________________________________________________

# ------- 
# Numbers
# -------

    if any(char.isdigit() for char in password):

        score += 1
        checks.append("Contains number: PASS")

    else:

        checks.append("Contains number: FAIL")

# _________________________________________________________________________________________________
    
# ------------------
# Special characters
# ------------------

    if any(char in string.punctuation for char in password):

        score += 1
        checks.append("Contains special character: PASS")

    else:

        checks.append("Contains special character: FAIL")

# _________________________________________________________________________________________________
    
# ---------------
# Password length
# --------------- 

    if len(password) >= 12:

        score += 1
        checks.append("At least 12 characters: PASS")

    else:

        checks.append("At least 12 characters: FAIL")

# _________________________________________________________________________________________________
