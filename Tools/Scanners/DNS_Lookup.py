# ======================================
# === Domain Name System Lookup Tool ===
# ======================================

# =======================
# === DNS Lookup Tool ===
# =======================

import socket

from shared.banner import show_banner
from shared.tables import print_section, print_analysis_complete
from shared.utils import pause


# _________________________________________________________________________________________________

def lookup_domain(domain):

    try:

        ip_address = socket.gethostbyname(domain)

        return {
            "Domain Name": domain,
            "IP Address": ip_address,
            "Status": "Resolved"
        }

    except socket.gaierror:

        return {
            "Domain Name": domain,
            "IP Address": "Unavailable",
            "Status": "Unable to resolve"
        }


# _________________________________________________________________________________________________
