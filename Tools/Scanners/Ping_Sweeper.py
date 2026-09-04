# ====================
# === Ping Sweeper ===
# ====================

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

def main():

    show_banner("Ping Sweeper")

    network = input("\nEnter network (e.g. 192.168.1): ").strip()

    print("\nSweeping network...\n")

    devices_found = ping_sweep(network)

    print("\n\nSweep Complete")

# _________________________________________________________________________________________________

    print_section(
        "Sweep Results",
        {
            "Network": network,
            "Devices Found": len(devices_found)
        }
    )

# _________________________________________________________________________________________________

    if devices_found:

        print("--- Online Devices ---\n")

        print(
            f"{'No.':<6}"
            f"{'IP Address'}"
        )

        print("-" * 30)

        for number, ip in enumerate(
            devices_found,
            start=1
        ):

            print(
                f"{number:<6}"
                f"{ip}"
            )

    else:

        print("No online devices were found.")

    analysis_complete = "Analysis Complete"
    
    print_analysis_complete(analysis_complete)

    pause()


if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________