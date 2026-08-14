# ======================
# === Ping Sweeper =====
# ======================

import subprocess

from Shared_Tools.Banner import show_banner
from Shared_Tools.Progress_Bar import progress
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause


# _________________________________________________________________________________________________

def ping_sweep(network):

    devices_found = []

    total = 254

    for i in range(1, 255):

        ip = f"{network}.{i}"

        progress(i, total)

        try:

            result = subprocess.run([
                    "ping",
                    "-n",
                    "1",
                    "-w",
                    "100",
                    ip
                ],
                capture_output=True,
                text=True
            )

            if "ttl=" in result.stdout.lower():

                devices_found.append(ip)

        except:
            pass

    return devices_found


# _________________________________________________________________________________________________
