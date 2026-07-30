# =============================
# === Cybersecurity Toolkit ===
# =============================

'''
Main Dashboard

Run : python dashboard.py
'''

# _________________________________________________________________________________________________

# ---------------
# Menue Utilities
# ---------------


def pause():
    input("\nPress Enter to continue")

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

# -----------------
# --- Main Loop ---
# -----------------


def main():

    while True:

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