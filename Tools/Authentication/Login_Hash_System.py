# =========================
# === Login Hash System ===
# =========================

import hashlib
import os

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

FILE_NAME = "users.txt"


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()

# _________________________________________________________________________________________________

def create_account():

    print("\n=== Create Account ===")

    username = input("Username: ").strip()

    password = input("Password: ")

    if not username or not password:

        print("\nUsername and password cannot be empty")

        return
    
# _________________________________________________________________________________________________

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            for line in file:

                saved_username = line.strip().split(":")[0]

                if username == saved_username:

                    print("\nUsername already exists:(")

                    return
                
# _________________________________________________________________________________________________

    password_hash = hash_password(password)

    with open(FILE_NAME, "a") as file:

        file.write(f"{username}:{password_hash}\n")

    print("\nAccount created successfully :)")

# _________________________________________________________________________________________________
