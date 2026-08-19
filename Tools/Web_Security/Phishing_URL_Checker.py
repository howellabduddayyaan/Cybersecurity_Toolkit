# ============================
# === Phishing URL Checker ===
# ============================

import re
from urllib.parse import urlparse

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "bank",
    "password",
    "confirm"
]

def is_ip(address):

    return re.match(
        r"^\d{1,3}(\.\d{1,3}){3}$",
        address
    ) is not None

# _________________________________________________________________________________________________

