# =====================
# === Caesar Cipher ===
# =====================

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause


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

def main():

    show_banner("Caesar Cipher")


    while True:

        choice = input("\nEncrypt or Decrypt? (e/d): ").lower().strip()

        if choice in ["e", "d"]:

            break

        print("Enter 'e' or 'd' only")

    message = input("Enter message: ")

    while True:

        try:

            shift = int(input("Enter shift value: "))

            break

        except ValueError:

            print("Enter a number")

    if choice == "e":

        output = caesar_cipher(message,shift,"encrypt")

        operation = "Encryption"

    else:

        output = caesar_cipher(message,shift,"decrypt")

        operation = "Decryption"

    print_section(
        "Caesar Cipher Result",
        {
            "Operation": operation,
            "Shift": shift,
            "Input": message,
            "Output": output
        }
    )

    analysis_complete = "Analysis Complete"
    
    print_analysis_complete(analysis_complete)

    pause()


if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________