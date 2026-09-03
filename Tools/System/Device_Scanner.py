# ======================
# === Device Scanner ===
# ======================

import socket
import uuid
import platform
import psutil

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete
from Shared_Tools.Menu_Utilities import pause


def get_device_information():

# --- Device Name ---

    device_name = socket.gethostname()
    
# _________________________________________________________________________________________________

# --- IP Address ---

    try:
        ip_address = socket.gethostbyname(device_name)
    except:
        ip_address = "Unavailable"

# _________________________________________________________________________________________________

# --- MAC Address ---

    mac = uuid.getnode()

    mac_address = ":".join(f"{(mac >> ele) & 0xff:02X}" for ele in range(40, -1, -8))

# _________________________________________________________________________________________________

# --- Operating System ---

    operating_system = (f"{platform.system()} {platform.release()}")

# _________________________________________________________________________________________________

# --- CPU Information ---

    processor = platform.processor()

    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)

    cpu_usage = psutil.cpu_percent(interval=1)

# _________________________________________________________________________________________________

# --- RAM Information ---

    memory = psutil.virtual_memory()

    total_ram = memory.total / (1024 ** 3)
    available_ram = memory.available / (1024 ** 3)
    used_ram = memory.used / (1024 ** 3)

# _________________________________________________________________________________________________

# --- Storage Information ---

    disk = psutil.disk_usage("/")

    total_storage = disk.total / (1024 ** 3)
    used_storage = disk.used / (1024 ** 3)
    free_storage = disk.free / (1024 ** 3)

# _________________________________________________________________________________________________

# --- Output ---

    return {
        "device": {
            "Device Name": device_name,
            "IP Address": ip_address,
            "MAC Address": mac_address,
            "Operating System": operating_system
        },

        "cpu": {
            "Processor": processor,
            "Physical Cores": physical_cores,
            "Logical Cores": logical_cores,
            "CPU Usage": f"{cpu_usage}%"
        },

        "memory": {
            "Installed RAM": f"{total_ram:.2f} GB",
            "Used RAM": f"{used_ram:.2f} GB",
            "Available RAM": f"{available_ram:.2f} GB"
        },

        "storage": {
            "Total Storage": f"{total_storage:.2f} GB",
            "Used Storage": f"{used_storage:.2f} GB",
            "Free Storage": f"{free_storage:.2f} GB"
        }
    }

# _________________________________________________________________________________________________

# --- Display Information ---

def main():

    show_banner("Device Scanner")

    information = get_device_information()

    print_section(
        "Device Information",
        information["device"]
    )

    print_section(
        "CPU",
        information["cpu"]
    )

    print_section(
        "Memory",
        information["memory"]
    )

    print_section(
        "Storage",
        information["storage"]
    )

    print_analysis_complete(analysis_complete)

    pause()


if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________