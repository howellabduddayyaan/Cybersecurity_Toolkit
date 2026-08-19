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

def check_url(url):

    risk_score = 0
    warnings = []

    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    hostname = parsed.hostname

    if hostname is None:

        return {
            "Risk Score": 0,
            "Risk Level": "Invalid URL",
            "Warnings": ["Unable to read hostname"]
        }
        
# _________________________________________________________________________________________________

    if is_ip(hostname):

        risk_score += 2

        warnings.append("URL uses an IP address")
        
# _________________________________________________________________________________________________

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in url.lower():

            risk_score += 1

            warnings.append(f"Suspicious keyword: {keyword}")
            
# _________________________________________________________________________________________________

    if "@" in url:

        risk_score += 2

        warnings.append("URL contains @ symbol")
        
# _________________________________________________________________________________________________

    if len(url) > 100:

        risk_score += 1

        warnings.append("URL is unusually long")
        
# _________________________________________________________________________________________________

    subdomains = hostname.split(".")

    if len(subdomains) > 3:

        risk_score += 1

        warnings.append("Too many subdomains")
        
# _________________________________________________________________________________________________

