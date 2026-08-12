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

def main():

    show_banner("Network Scanner")

    network = input("\nEnter network (e.g. 192.168.1): ").strip()

    # _________________________________________________________________________________________________

    try:

        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

    except:

        hostname = "Unavailable"
        local_ip = "Unavailable"

    # _________________________________________________________________________________________________

    print_section(
        "Local Device",
        {
            "Hostname": hostname,
            "IP Address": local_ip
        }
    )

    print("\nScanning network...\n")

    # _________________________________________________________________________________________________

    devices = scan_network(network)

    print("\n\nScan Complete")

    # _________________________________________________________________________________________________

    print_section(
        "Scan Results",
        {
            "Network": network,
            "Devices Found": len(devices)
        }
    )

    # _________________________________________________________________________________________________

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

    # _________________________________________________________________________________________________

    print_analysis_complete()

    pause()

# _________________________________________________________________________________________________

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________