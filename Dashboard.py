# ===============================
# === Cybersecurity Dashboard ===
# ===============================

'''
Main Dashboard

Run : python dashboard.py
'''

import os

# _________________________________________________________________________________________________

# ---------------
# Menue Utilities
# ---------------


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue")
    
def banner():

    print('''
|=================================================================================================|
|======================================= Cybersecurity Toolkit ===================================|
|=================================================================================================|
    ''')

# _________________________________________________________________________________________________

# --------------
# Tool Functions
# --------------


def device_scanner():
    print("\nLaunching Device Scanner...")
    

def network_scanner():
    print("\nLaunching Network Scanner...")


def port_scanner():
    print("\nLaunching Port Scanner...")


def packet_sniffer():
    print("\nLaunching Packet Sniffer...")


def dns_lookup():
    print("\nLaunching DNS Lookup...")


def phishing_checker():
    print("\nLaunching Phishing URL Checker...")


def ssl_checker():
    print("\nLaunching SSL Certificate Checker...")


def whois_lookup():
    print("\nLaunching WHOIS Lookup...")


def login_system():
    print("\nLaunching Login System...")


def password_manager():
    print("\nLaunching Password Manager...")


def password_strength():
    print("\nLaunching Password Strength Checker...")


def file_hash():
    print("\nLaunching File Hash Checker...")


def caesar_cipher():
    print("\nLaunching Caesar Cipher...")


def base64_tool():
    print("\nLaunching Base64 Encoder / Decoder...")


def log_analyzer():
    print("\nLaunching Log Analyzer...")


def brute_force():
    print("\nLaunching Brute Force Simulator...")

# _________________________________________________________________________________________________

# ---------
# Dashboard
# ---------


def show_menu():

    banner()

    print('''
|-------------------------------------------------------------------------------------------------|
|                                        SYSTEM                                                   |
|-------------------------------------------------------------------------------------------------|
| 1. | Device Scanner                                                                             |
|-------------------------------------------------------------------------------------------------|
|                                       NETWORK                                                   |
|-------------------------------------------------------------------------------------------------|
| 2. | Network Scanner                                                                            |
| 3. | Port Scanner                                                                               |
| 4. | Packet Sniffer                                                                             |
| 5. | DNS Lookup                                                                                 |
|-------------------------------------------------------------------------------------------------|
|                                     WEB SECURITY                                                |
|-------------------------------------------------------------------------------------------------|
| 6. Phishing URL Checker                                                                         |
| 7. SSL Certificate Checker                                                                      |
| 8. WHOIS Lookup                                                                                 |
|-------------------------------------------------------------------------------------------------|
|                                    AUTHENTICATION                                               |
|-------------------------------------------------------------------------------------------------|
| 9. Login System                                                                                 |
| 10. Password Manager                                                                            |
|-------------------------------------------------------------------------------------------------|
|                                    PASSWORD TOOLS                                               |
|-------------------------------------------------------------------------------------------------|
| 11. Password Strength Checker                                                                   |
| 12. File Hash Checker                                                                           |
|-------------------------------------------------------------------------------------------------|
|                                    CRYPTOGRAPHY
|-------------------------------------------------------------------------------------------------|
| 13. Caesar Cipher
| 14. Base64 Encoder / Decoder
|-------------------------------------------------------------------------------------------------|
|                                     ANALYSIS
|-------------------------------------------------------------------------------------------------|
| 15. Log Analyzer
|-------------------------------------------------------------------------------------------------|
|                                    SIMULATORS
|-------------------------------------------------------------------------------------------------|
| 16. Brute Force Simulator
|-------------------------------------------------------------------------------------------------|
|-------------------------------------------------------------------------------------------------|
| 0. Exit
|-------------------------------------------------------------------------------------------------|
''')

# _________________________________________________________________________________________________

# -----------------
# --- Main Loop ---
# -----------------


def main():

    while True:
        
        show_menu()

        choice = input("Choose an option : ")

        if choice == "1":
            device_scanner()

        elif choice == "2":
            network_scanner()

        elif choice == "3":
            port_scanner()

        elif choice == "4":
            packet_sniffer()

        elif choice == "5":
            dns_lookup()

        elif choice == "6":
            phishing_checker()

        elif choice == "7":
            ssl_checker()

        elif choice == "8":
            whois_lookup()

        elif choice == "9":
            login_system()

        elif choice == "10":
            password_manager()

        elif choice == "11":
            password_strength()

        elif choice == "12":
            file_hash()

        elif choice == "13":
            caesar_cipher()

        elif choice == "14":
            base64_tool()

        elif choice == "15":
            log_analyzer()

        elif choice == "16":
            brute_force()

        elif choice == "17":

            print("\nGoodbye :)")
            break

        else:
            print("\nInvalid option")
            pause()


if __name__ == "__main__":
    main()

# _________________________________________________________________________________________________