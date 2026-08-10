# ======================
# === Device Scanner ===
# ======================

import socket
import uuid
import platform
import psutil

from shared.banner import show_banner
from shared.tables import print_table
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