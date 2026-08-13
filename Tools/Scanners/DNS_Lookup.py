# ======================================
# === Domain Name System Lookup Tool ===
# ======================================

import socket

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

# --- Check Domain ---

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

# --- Display ---

def main():

    show_banner("DNS Lookup Tool")

    domain = input(
        "\nEnter a domain (e.g. google.com): "
    ).strip()

    if not domain:

        print("\nPlease enter a domain.")

        pause()

        return

    information = lookup_domain(domain)

# _________________________________________________________________________________________________

    print_section(
        "DNS Information",
        information
    )

    print_analysis_complete()

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________