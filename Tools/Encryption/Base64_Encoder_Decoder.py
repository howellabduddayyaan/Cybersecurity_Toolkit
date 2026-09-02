# ==============================
# === Base64 Encoder/Decoder ===
# ==============================

import base64

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

def encode_text():

    text = input("\nEnter text to encode: ")

    encoded = base64.b64encode(text.encode()).decode()

    print_section(
        "Base64 Encoding",
        {
            "Input": text,
            "Encoded": encoded
        }
    )

# _________________________________________________________________________________________________

def decode_text():

    text = input("\nEnter Base64 text to decode: ")

    try:

        decoded = base64.b64decode(text, validate=True).decode()

        print_section(
            "Base64 Decoding",
            {
                "Encoded": text,
                "Decoded": decoded
            }
        )

    except Exception:

        print("\nError: Invalid Base64 input")


# _________________________________________________________________________________________________


def main():

    show_banner("Base64 Encoder / Decoder")

    while True:

        print("""
1. Encode
2. Decode
3. Exit
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":

            encode_text()

        elif choice == "2":

            decode_text()

        elif choice == "3":

            print("\nGoodbye")

            break

        else:

            print("\nInvalid choice")

    print_analysis_complete()

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________