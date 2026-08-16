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

def main():

    show_banner("Port Scanner")

    host = input("\nEnter an IP address or website: ").strip()

    try:

        start_port = int(input("Enter starting port: "))

        end_port = int(input("Enter ending port: "))

    except ValueError:

        print("\nPlease enter valid port numbers.")

        pause()

        return

    # _________________________________________________________________________________________________

    if (
        start_port < 1
        or end_port > 65535
        or start_port > end_port
    ):

        print(
            "\nPort numbers must be between "
            "1 and 65535."
        )

        pause()

        return

    # _________________________________________________________________________________________________

    print(f"\nScanning {host}...\n")

    open_ports = []

    try:

        for port in range(start_port,end_port + 1):

            if scan_port(host,port):

                open_ports.append(port)

        if not open_ports:

            print(
                "\nNo open ports found "
                "in the specified range."
            )

# _________________________________________________________________________________________________

        print_section(
            "Scan Results",
            {
                "Host": host,
                "Starting Port": start_port,
                "Ending Port": end_port,
                "Open Ports": len(open_ports)
            }
        )

        if open_ports:

            print("--- Open Ports ---\n")

            print(
                f"{'Port':<10}"
                f"Status"
            )

            print("-" * 25)

            for port in open_ports:

                print(
                    f"{port:<10}"
                    f"OPEN"
                )

        print_analysis_complete()

# _________________________________________________________________________________________________

    except KeyboardInterrupt:

        print("\n\nScan stopped by user")

    except socket.gaierror:

        print("\nInvalid host name")

    pause()

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________

"""

IP Address

"""