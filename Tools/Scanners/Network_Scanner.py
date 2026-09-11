# =======================
# === Network Scanner ===
# =======================

import socket
import subprocess

from Shared_Tools.Banner import show_banner
from Shared_Tools.Progress_Bar import progress
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause

# --- Scan Network ---

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

def main():

    show_banner("Network Scanner")

    network = input("\nEnter network (e.g. 192.168.1): ").strip()

# --- Local Device ---

    try:

        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

    except:

        hostname = "Unavailable"
        local_ip = "Unavailable"


    print_section(
        "Local Device",
        {
            "Hostname": hostname,
            "IP Address": local_ip
        }
    )

    print("\nScanning network...\n")

    devices = scan_network(network)

    print("\n\nScan Complete")


    print_section(
        "Scan Results",
        {
            "Network": network,
            "Devices Found": len(devices)
        }
    )

# --- Display Devices ---

    if devices:

        print("--- Devices ---\n")

        print(
            f"{'No.':<6}"
            f"{'Hostname':<30}"
            f"IP Address"
        )

        print("-" * 60)

        for number, (ip, hostname) in enumerate(
            devices,
            start=1
        ):

            print(
                f"{number:<6}"
                f"{hostname:<30}"
                f"{ip}"
            )

    else:

        print("\nNo devices were found")

    analysis_complete = "Analysis Complete"
    
    print_analysis_complete(analysis_complete)

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________