# =====================
# === Configuration ===
# =====================

from pathlib import Path

# -------------------
# Project Information
# -------------------

APP_NAME = "Cybersecurity Toolkit"
VERSION = "1.0.0"
AUTHOR = "Abdud Dayyaan Howell"

# _________________________________________________________________________________________________

# -------------
# Project Paths
# -------------

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
EXPORTS_DIR = ASSETS_DIR / "exports"

# Storage Vault

SAMPLE_DOMAINS = ASSETS_DIR / "sample_domains.txt"
TEST_URLS = ASSETS_DIR / "test_urls.txt"
SAMPLE_LOGS = ASSETS_DIR / "sample_logs.txt"
COMMON_PASSWORDS = ASSETS_DIR / "common_passwords.txt"

USERS_FILE = BASE_DIR / "users.txt"
VAULT_FILE = BASE_DIR / "vault.txt"

# _________________________________________________________________________________________________

# ----------------
# Scanner Settings
# ----------------

DEFAULT_TIMEOUT = 180.0            # Seconds (3mins)
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024

DEFAULT_NETWORK_RANGE = 254

# _________________________________________________________________________________________________

# -----------------
# Password Settings
# -----------------

DEFAULT_PASSWORD_LENGTH = 16
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64

# _________________________________________________________________________________________________

# ------------
# Progress Bar
# ------------

PROGRESS_BAR_WIDTH = 30

# _________________________________________________________________________________________________

# -----
# Ports
# -----

COMMON_PORTS = {20 : "FTP Data",
                21 : "FTP",
                22 : "SSH",
                23 : "Telnet",
                25 : "SMTP",
                53 : "DNS",
                67 : "DHCP",
                68 : "DHCP",
                69 : "TFTP",
                80 : "HTTP",
                110 : "POP3",
                123 :"NTP",
                143 : "IMAP",
                161 : "SNMP",
                389 : "LDAP",
                443 : "HTTPS",
                445 : "SMB",
                587 : "SMTP TLS",
                993 : "IMAPS",
                995 : "POP3S",
                1433 : "MSSQL",
                1521 : "Oracle",
                3306 : "MySQL",
                3389 : "RDP",
                5432 : "PostgreSQL",
                5900 : "VNC",
                6379 : "Redis",
                8080 : "HTTP Alternate"
                }

# _________________________________________________________________________________________________