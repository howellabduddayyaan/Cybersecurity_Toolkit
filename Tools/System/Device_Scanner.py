# ======================
# === Device Scanner ===
# ======================

import socket
import uuid
import platform
import psutil

from shared.banner import show_banner
from shared.tables import print_table, print_analysis_complete
from shared.utils import pause


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

