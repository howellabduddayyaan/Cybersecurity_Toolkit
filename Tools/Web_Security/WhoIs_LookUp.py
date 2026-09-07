# =========================
# === WHOIS Lookup Tool ===
# =========================

import whois

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

def clean(value):

    if isinstance(value, list):

        if len(value) > 0:
            value = value[0]

        else:
            return "Unavailable"

    if hasattr(value, "strftime"):

        return value.strftime("%d %B %Y")

    if value is None:

        return "Unavailable"

    return value

# _________________________________________________________________________________________________

def lookup_domain(domain):

    try:

        information = whois.whois(domain)

        return {
            "Domain Name": clean(information.domain_name),
            "Registrar": clean(information.registrar),
            "Created": clean(information.creation_date),
            "Expires": clean(information.expiration_date),
            "Name Servers": clean(information.name_servers),
            "Status": clean(information.status)
        }

    except Exception as error:

        return {
            "Domain Name": domain,
            "Status": "Lookup failed",
            "Error": str(error)
        }

# _________________________________________________________________________________________________

def main():

    show_banner("WHOIS Lookup Tool")

    domain = input("\nEnter a domain (e.g. tryhackme.com): ").strip()

    if not domain:

        print("\nPlease enter a domain.")

        pause()

        return

    print(f"\nLooking up {domain}...\n")

    information = lookup_domain(domain)

    print_section(
        "WHOIS Information",
        information
    )

    print_analysis_complete("Analysis Complete")

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________