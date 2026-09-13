# ===============================
# === SSL Certificate Checker ===
# ===============================

# --------------------
# Secure Sockets Layer
# --------------------

import socket
import ssl
from datetime import datetime, UTC

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# --- Check SSL Certificate ---

def check_ssl_certificate(domain):

    context = ssl.create_default_context()

    try:

        with socket.create_connection((domain, 443),timeout=5) as connection:

            with context.wrap_socket(connection,server_hostname=domain) as secure_socket:

                certificate = secure_socket.getpeercert()

# --- Certificate Information ---

        issuer = certificate.get("issuer","Unavailable")

        subject = certificate.get("subject","Unavailable")

        valid_from = certificate.get("notBefore","Unavailable")

        valid_until = certificate.get("notAfter","Unavailable")

# --- Certificate Results ---

        return {
            "Domain": domain,
            "Status": "Certificate Retrieved",
            "Issuer": issuer,
            "Subject": subject,
            "Valid From": valid_from,
            "Valid Until": valid_until
        }

    except socket.gaierror:

        return {
            "Domain": domain,
            "Status": "Invalid domain"
        }

    except socket.timeout:

        return {
            "Domain": domain,
            "Status": "Connection timed out"
        }

    except ssl.SSLError as error:

        return {
            "Domain": domain,
            "Status": f"SSL Error: {error}"
        }

    except Exception as error:

        return {
            "Domain": domain,
            "Status": f"Error: {error}"
        }

# --- Check Certificate Expiry ---

def check_certificate_expiry(valid_until):

    if valid_until == "Unavailable":

        return "Unavailable"

    try:

        expiry_date = datetime.strptime(valid_until,"%b %d %H:%M:%S %Y %Z").replace(tzinfo=UTC)

        current_date = datetime.now(UTC)

        if expiry_date < current_date:

            return "EXPIRED"

        remaining_days = (expiry_date - current_date).days

        return f"{remaining_days} days remaining"

    except:

        return "Unable to determine"

# _________________________________________________________________________________________________

def main():

    show_banner("SSL Certificate Checker")

    domain = input("\nEnter a domain (e.g. google.com): ").strip()

    if not domain:

        print("\nPlease enter a domain")

        pause()

        return

# _________________________________________________________________________________________________

    print(f"\nChecking SSL certificate for {domain}...\n")

    certificate = check_ssl_certificate(domain)


# --- Check Errors ---

    if certificate["Status"] != "Certificate Retrieved":

        print_section("SSL Certificate",certificate)

        print_analysis_complete()

        pause()

        return

# --- Expiry Status ---

    expiry_status = check_certificate_expiry(
        certificate["Valid Until"]
    )

    print_section(
        "SSL Certificate",
        {
            "Domain": certificate["Domain"],
            "Status": certificate["Status"],
            "Valid From": certificate["Valid From"],
            "Valid Until": certificate["Valid Until"],
            "Expiry Status": expiry_status
        }
    )

    print_section(
        "Certificate Details",
        {
            "Issuer": certificate["Issuer"],
            "Subject": certificate["Subject"]
        }
    )

    print_analysis_complete("Analysis Complete")

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________