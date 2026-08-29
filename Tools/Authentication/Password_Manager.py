# ========================
# === Password Manager ===
# ========================

import hashlib
import os
import string
import secrets

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

VAULT_FILE = "vault.txt"

MASTER_PASSWORD = "Doodle"


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


MASTER_HASH = hash_password(MASTER_PASSWORD)


# _________________________________________________________________________________________________

def login():

    print("\n=== Login ===")

    password = input("Enter master password: ")

    if hash_password(password) == MASTER_HASH:

        print("\nLogin Successful :)")

        return True

    print("\nIncorrect password :(")

    return False

# _________________________________________________________________________________________________

def add_password():

    print("\n=== Add Password ===")

    website = input("Website : ").strip()

    username = input("Username: ").strip()

    password = input("Password: ")

    if not website or not username or not password:

        print("\nAll fields are required")

        return

    with open(VAULT_FILE,"a") as file:

        file.write(f"{website}|{username}|{password}\n")

    print("\nPassword saved successfully :)")

# _________________________________________________________________________________________________
