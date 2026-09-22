=======================
# Cybersecurity Toolkit
=======================

This is a modular, terminal-based Cybersecurity Toolkit built in Python. This toolkit provides a suite of practical security tools—ranging from network scanning and web reconnaissance to password auditing, encryption, and attack simulations—organized into a clean, intuitive menu system

# --- Project Overview ---

- Author: Abdud Dayyaan Howell
- Version: 1.0.0
- Language: Python 3.x
- Interface: Terminal / CLI Dashboard

# --- Toolkit Features ---

The toolkit is divided into categorized modules designed to keep the terminal dashboard neat, structured, and readable:

# 1. System

Device Scanner – Inspects local system configuration, host details, and active network interfaces

# 2. Scanners

Network Scanner – Scans local IP ranges to identify active hosts on the network
Port Scanner – Probes target IPs for open ports against common services
Packet Sniffer – Captures and inspects live IP, TCP, UDP, and ICMP network traffic
DNS Lookup – Resolves hostnames to IP addresses and extracts DNS records
Ping Sweeper – Sweeps target subnets to detect responsive devices via ICMP echo requests

# 3. Web Security

Phishing URL Checker – Inspects URLs for suspicious patterns, IP-based hosts, and high-risk keywords
SSL Certificate Checker – Validates SSL/TLS certificate validity, issuer, and expiration dates
WHOIS Lookup – Retrieves domain registrar, creation dates, and administrative details

# 4. Authentication

Login System – Demonstrates secure user authentication utilizing salting and SHA-256 hashing
Password Manager – Encrypted credential vault allowing master-key-protected secret storage

# 5. Password Tools

Password Strength Checker – Evaluates password complexity, entropy, character variety, and common vulnerabilities

# 6. Encryption

Caesar Cipher – Classic substitution cipher for encrypting and decrypting text with arbitrary shift values
Base64 Encoder/Decoder – Quick encoding and decoding of plain text and binary representations

# 7. Analysis

Log Analyzer – Parses log files to detect suspicious activity, brute-force attempts, and failed requests

# 8. Simulators

Brute Force Simulator – Educational attack simulator illustrating password cracking speed and permutation complexity

# --- Project Structure ---

    Cybersecurity_Toolkit/
    │
    ├── Dashboard.py              # Main terminal dashboard entry point
    ├── Config.py                 # Global configuration, port lists, and settings
    ├── users.txt                 # User store for login system
    ├── vault.txt                 # Encrypted storage vault
    │
    ├── Assets/                   # Wordlists and test resources
    │   ├── Common_Passwords.txt
    │   ├── Sample_Domains.txt
    │   ├── Sample_Logs.txt
    │   ├── Test_Urls.txt
    │   └── Wordlist.txt
    │
    ├── Shared_Tools/             # Reusable UI & terminal utilities
    │   ├── Banner.py             # 80-character standardized banners
    │   ├── File_Manager.py       # File reading & writing helpers
    │   ├── Menu_Utilities.py     # Terminal clear and pause utilities
    │   ├── Network.py            # Network helper routines
    │   ├── Progress_Bar.py       # Terminal progress bar component
    │   ├── Tables.py             # Formatted data tables & result banners
    │   └── Validators.py         # Input validation helpers
    │
    └── Tools/                    # Tool categories and implementations
        ├── Analysis/             # Log Analyzer
        ├── Authentication/       # Login System & Password Manager
        ├── Encryption/           # Caesar Cipher & Base64 Encoder/Decoder
        ├── Password_Tools/       # Password Strength Checker
        ├── Scanners/             # Network, Port, Sniffer, DNS, Ping Sweeper
        ├── Simulation/           # Brute Force Simulator
        ├── System/               # Device Scanner
        └── Web_Security/         # Phishing Checker, SSL Checker, WHOIS

# --- Prerequisites ---

Ensure you have Python 3.10+ installed. Some networking and reconnaissance tools require third-party libraries:

pip install scapy python-whois

Note on Packet Sniffing / Raw Sockets: Running the Packet Sniffer or low-level socket operations may require
elevated/administrator privileges on Windows or root privileges (sudo) on Linux

# --- Running the Toolkit ---

Launch the main interactive dashboard:

python dashboard.py

# Disclaimer

This toolkit was created for educational, defensive, and authorized administrative testing purposes only. Do not scan or
target systems, domains, or networks without explicit written permission from the owner.

# --- Demo video ---

https://youtu.be/c_53bVrxOX8

# --- Repository code ---

WTC-4RPCX3WC

# _______________________________________________________________________________________________________________________________
