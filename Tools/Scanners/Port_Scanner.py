# ====================
# === Port Scanner ===
# ====================

import socket

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# _________________________________________________________________________________________________

def scan_port(host, port):

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    sock.settimeout(0.5)

    try:

        result = sock.connect_ex((host, port))

        if result == 0:

            print(f"Port {port:<6}: OPEN")

            return True

        return False

    finally:

        sock.close()

# _________________________________________________________________________________________________
