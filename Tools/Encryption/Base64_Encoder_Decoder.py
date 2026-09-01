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

