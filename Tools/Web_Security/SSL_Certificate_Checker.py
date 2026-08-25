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

# _________________________________________________________________________________________________

def check_ssl_certificate(domain):

    context = ssl.create_default_context()

    try:

        with socket.create_connection((domain, 443),timeout=5) as connection:

            with context.wrap_socket(connection,server_hostname=domain) as secure_socket:

                certificate = secure_socket.getpeercert()

# _________________________________________________________________________________________________

        issuer = certificate.get("issuer","Unavailable")

        subject = certificate.get("subject","Unavailable")

        valid_from = certificate.get("notBefore","Unavailable")

        valid_until = certificate.get("notAfter","Unavailable")

# _________________________________________________________________________________________________

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


# _________________________________________________________________________________________________

