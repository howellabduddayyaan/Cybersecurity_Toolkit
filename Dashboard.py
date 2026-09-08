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
    
# # def banner():

# #     print('''
# # |=================================================================================================|
# # |======================================= Cybersecurity Toolkit ===================================|
# # |=================================================================================================|
#     ''')

# _________________________________________________________________________________________________

# --------------
# Tool Functions
# --------------


def device_scanner():
    clear()
    print("\nLaunching Device Scanner...")
    device_scanner_main()
    pause()
    

def network_scanner():
    clear()
    print("\nLaunching Network Scanner...")
    network_scanner_main()
    pause()


def port_scanner():
    clear()
    print("\nLaunching Port Scanner...")
    port_scanner_main()
    pause()

def packet_sniffer():
    clear()
    print("\nLaunching Packet Sniffer...")
    packet_sniffer_main()
    pause()


def dns_lookup():
    clear()
    print("\nLaunching DNS Lookup...")
    dns_lookup_main()
    pause()


def phishing_checker():
    clear()
    print("\nLaunching Phishing URL Checker...")
    phishing_checker_main()
    pause()


def ssl_checker():
    clear()
    print("\nLaunching SSL Certificate Checker...")
    ssl_checker_main()
    pause()


def whois_lookup():
    clear()
    print("\nLaunching WHOIS Lookup...")
    whois_lookup_main()
    pause()


def login_system():
    clear()
    print("\nLaunching Login System...")
    login_system_main()
    pause()


def password_manager():
    clear()
    print("\nLaunching Password Manager...")
    password_manager_main()
    pause()


def password_strength():
    clear()
    print("\nLaunching Password Strength Checker...")
    password_strength_main()
    pause()


def caesar_cipher():
    clear()
    print("\nLaunching Caesar Cipher...")
    caesar_cipher_main()
    pause()


def base64_tool():
    clear()
    print("\nLaunching Base64 Encoder / Decoder...")
    base64_tool_main()
    pause()


def log_analyzer():
    clear()
    print("\nLaunching Log Analyzer...")
    log_analyzer_main()
    pause()

def brute_force():
    clear()
    print("\nLaunching Brute Force Simulator...")
    brute_force_main()
    pause()

# _________________________________________________________________________________________________

# -----------
# System Menu
# -----------


def system_menu():

    while True:

        clear()

        print('''
===============================================================================
                                SYSTEM
===============================================================================

1. | Device Scanner

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            device_scanner()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# -------------
# Scanners Menu
# -------------


def scanners_menu():

    while True:

        clear()

        print('''
===============================================================================
                                SCANNERS
===============================================================================

1. | Network Scanner
2. | Port Scanner
3. | Packet Sniffer
4. | DNS Lookup

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            network_scanner()

        elif choice == "2":
            port_scanner()

        elif choice == "3":
            packet_sniffer()

        elif choice == "4":
            dns_lookup()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# -----------------
# Web Security Menu
# -----------------


def web_security_menu():

    while True:

        clear()

        print('''
===============================================================================
                             WEB SECURITY
===============================================================================

1. | Phishing URL Checker
2. | SSL Certificate Checker
3. | WHOIS Lookup

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            phishing_checker()

        elif choice == "2":
            ssl_checker()

        elif choice == "3":
            whois_lookup()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# -------------------
# Authentication Menu
# -------------------


def authentication_menu():

    while True:

        clear()

        print('''
===============================================================================
                            AUTHENTICATION
===============================================================================

1. | Login System
2. | Password Manager

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            login_system()

        elif choice == "2":
            password_manager()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# -------------------
# Password Tools Menu
# -------------------

def password_tools_menu():

    while True:

        clear()

        print('''
===============================================================================
                           PASSWORD TOOLS
===============================================================================

1. | Password Strength Checker

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            password_strength()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# ---------------
# Encryption Menu
# ---------------


def encryption_menu():

    while True:

        clear()

        print('''
===============================================================================
                             ENCRYPTION
===============================================================================

1. | Caesar Cipher
2. | Base64 Encoder / Decoder

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            caesar_cipher()

        elif choice == "2":
            base64_tool()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# -------------
# Analysis Menu
# -------------


def analysis_menu():

    while True:

        clear()

        print('''
===============================================================================
                              ANALYSIS
===============================================================================

1. | Log Analyzer

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            log_analyzer()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# ---------------
# Simulation Menu
# ---------------


def simulation_menu():

    while True:

        clear()

        print('''
===============================================================================
                             SIMULATORS
===============================================================================

1. | Brute Force Simulator

-------------------------------------------------------------------------------

0. | Back

===============================================================================
''')

        choice = input("Choose an option : ")

        if choice == "1":
            brute_force()

        elif choice == "0":
            break

        else:
            print("\nInvalid option")
            pause()


# _________________________________________________________________________________________________

# --------------
# Main Dashboard
# --------------

def show_menu():

    print('''
===============================================================================
                         CYBERSECURITY TOOLKIT
===============================================================================

1. | System
2. | Scanners
3. | Web Security
4. | Authentication
5. | Password Tools
6. | Encryption
7. | Analysis
8. | Simulators

-------------------------------------------------------------------------------

0. | Exit

===============================================================================
''')


# _________________________________________________________________________________________________

# ---------
# Main Loop
# ---------

def main():

    while True:

        clear()

        show_menu()

        choice = input("Choose a folder : ")

        if choice == "1":
            system_menu()

        elif choice == "2":
            scanners_menu()

        elif choice == "3":
            web_security_menu()

        elif choice == "4":
            authentication_menu()

        elif choice == "5":
            password_tools_menu()

        elif choice == "6":
            encryption_menu()

        elif choice == "7":
            analysis_menu()

        elif choice == "8":
            simulation_menu()

        elif choice == "0":

            clear()
            print("\nGoodbye :)")
            break

        else:
            print("\nInvalid option")
            pause()

if __name__ == "__main__":
    main()

# _________________________________________________________________________________________________