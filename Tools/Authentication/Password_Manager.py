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

def view_passwords():

    print("\n=== Saved Passwords ===")

    if not os.path.exists(VAULT_FILE):

        print("\nNo passwords are saved :(")

        return

    with open(VAULT_FILE,"r") as file:

        entries = file.readlines()

    if not entries:

        print("\nNo passwords are saved :(")

        return

    print()

    print(
        f"{'No.':<6}"
        f"{'Website':<25}"
        f"{'Username':<25}"
        f"Password"
    )

    print("-" * 75)

    for number, entry in enumerate(entries,start=1):

        parts = entry.strip().split("|")

        if len(parts) != 3:
            continue

        website, username, password = parts

        print(
            f"{number:<6}"
            f"{website:<25}"
            f"{username:<25}"
            f"{password}"
        )

# _________________________________________________________________________________________________

def search_password():

    print("\n=== Search Password ===")

    website = input("Enter website: ").strip()

    if not os.path.exists(VAULT_FILE):

        print("\nNo passwords are saved :(")

        return

    found = False

    with open(VAULT_FILE,"r") as file:

        for entry in file:

            parts = entry.strip().split("|")

            if len(parts) != 3:
                continue

            saved_website, username, password = parts

            if website.lower() == saved_website.lower():

                print_section(
                    "Password Found",
                    {
                        "Website": saved_website,
                        "Username": username,
                        "Password": password
                    }
                )

                found = True

    if not found:

        print("\nWebsite not found")

# _________________________________________________________________________________________________

def delete_password():

    print("\n=== Delete Password ===")

    website = input("Enter website: ").strip()

    if not os.path.exists(VAULT_FILE):

        print("\nNo passwords are saved :(")

        return

    with open(VAULT_FILE,"r") as file:

        entries = file.readlines()

    deleted = False

    with open(VAULT_FILE,"w") as file:

        for entry in entries:

            saved_website = (entry.split("|")[0])

            if (saved_website.lower()!= website.lower()):

                file.write(entry)

            else:

                deleted = True

    if deleted:

        print("\nPassword deleted")

    else:

        print("\nWebsite not found")

# _________________________________________________________________________________________________

def generate_password():

    print("\n=== Password Generator ===")

    try:

        length = int(input("Password length: "))

        if length <= 0:

            print("\nEnter a number greater than 0")

            return

        characters = (string.ascii_letters + string.digits + "!@#$%^&*()")

        password = "".join(secrets.choice(characters) for _ in range(length))

        print_section(
            "Generated Password",
            {
                "Length": length,
                "Password": password
            }
        )

    except ValueError:

        print("\nPlease enter a valid number")

# _________________________________________________________________________________________________

def password_manager():

    while True:

        print("""
================================
=== Secure Password Manager ====
================================

1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Generate Password
6. Exit
""")

        choice = input("Choose an option: ").strip()

# _________________________________________________________________________________________________

        if choice == "1":

            add_password()

        elif choice == "2":

            view_passwords()

        elif choice == "3":

            search_password()

        elif choice == "4":

            delete_password()

        elif choice == "5":

            generate_password()

        elif choice == "6":

            print("\nGoodbye")

            break

        else:

            print("\nInvalid option :(")

# _________________________________________________________________________________________________

def main():

    show_banner("Password Manager")

    if login():

        password_manager()

    analysis_complete = "Analysis Complete"

    print_analysis_complete(analysis_complete)

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________