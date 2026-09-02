# ===============================
# === Cybersecurity Dashboard ===
# ===============================

'''
Main Dashboard

Run : python dashboard.py
'''

import os

from Tools.System.Device_Scanner import main as device_scanner_main

from Tools.Scanners.Network_Scanner import main as network_scanner_main
from Tools.Scanners.Port_Scanner import main as port_scanner_main
from Tools.Scanners.Packet_Sniffer import main as packet_sniffer_main
from Tools.Scanners.DNS_Lookup import main as dns_lookup_main

from Tools.Web_Security.Phishing_URL_Checker import main as phishing_checker_main
from Tools.Web_Security.SSL_Certificate_Checker import main as ssl_checker_main
from Tools.Web_Security.WhoIs_LookUp import main as whois_lookup_main

from Tools.Authentication.Login_Hash_System import main as login_system_main
from Tools.Authentication.Password_Manager import main as password_manager_main

from Tools.Password_Tools.Password_Strength_Checker import main as password_strength_main

from Tools.Encryption.Caesar_Cipher import main as caesar_cipher_main
from Tools.Encryption.Base64_Encoder_Decoder import main as base64_tool_main

from Tools.Analysis.Log_Analyzer import main as log_analyzer_main

from Tools.Simulation.Brute_Force_Simulator import main as brute_force_main

# _________________________________________________________________________________________________

# ---------------
# Menu Utilities
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
    device_scanner_main()
    

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