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

def login():

    print("\n=== Login ===")

    username = input("Username: ").strip()

    password = input("Password: ")

    if not os.path.exists(FILE_NAME):

        print("\nNo users have been registered :(")

        return False

    password_hash = hash_password(password)

# _________________________________________________________________________________________________

    with open(FILE_NAME, "r") as file:

        for line in file:

            parts = line.strip().split(":")

            if len(parts) != 2:
                continue

            saved_username = parts[0]
            saved_hash = parts[1]

            if (username == saved_username and password_hash == saved_hash):

                print_section(
                    "Login Result",
                    {
                        "Username": username,
                        "Status": "Login Successful :)"
                    }
                )

                return True

# _________________________________________________________________________________________________

    print_section(
        "Login Result",
        {
            "Username": username,
            "Status": "Invalid username or password"
        }
    )

    return False

# _________________________________________________________________________________________________


def main():

    show_banner("Login Hash System")

    while True:

        print("""
| 1 | Create Account
| 2 | Login
| 3 | Exit
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":

            create_account()

        elif choice == "2":

            login()

        elif choice == "3":

            print("\nGoodbye")

            break

        else:

            print("\nInvalid choice :(")

    analysis_complete = "Analysis Complete"
    
    print_analysis_complete(analysis_complete)

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________
