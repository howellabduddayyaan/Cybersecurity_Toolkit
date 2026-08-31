# =====================
# === Caesar Cipher ===
# =====================

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

def caesar_cipher(text, shift, mode):

    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:

        if char.isalpha():

            if char.isupper():

                new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))

            else:

                new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))

            result += new_char

        else:

            result += char

    return result

# _________________________________________________________________________________________________

