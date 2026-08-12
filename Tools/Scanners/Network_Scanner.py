# =======================
# === Network Scanner ===
# =======================

import socket
import subprocess

from shared.banner import show_banner
from shared.progress import progress
from shared.tables import print_section, print_analysis_complete
from shared.utils import pause


# _________________________________________________________________________________________________

def scan_network(network):

    devices = []

    total = 254

    for i in range(1, 255):

        ip = f"{network}.{i}"

        progress(i, total)

        try:

            result = subprocess.run(["ping","-n","1","-w","100",ip],
                                    capture_output=True,
                                    text=True
                                    )

            if "ttl=" in result.stdout.lower():

                try:
                    hostname = socket.gethostbyaddr(ip)[0]

                except:
                    hostname = "Unknown"

                devices.append((ip, hostname))

        except:
            pass

    return devices


# _________________________________________________________________________________________________
