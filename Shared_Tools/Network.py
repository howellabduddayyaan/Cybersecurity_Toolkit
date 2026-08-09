# =======================
# === Host Identifier ===
# =======================

import socket

def get_local_ip():

    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

    except:
        return "Unavailable"


def get_hostname(ip):

    try:
        return socket.gethostbyaddr(ip)[0]

    except:
        return "Unknown"
    
# _________________________________________________________________________________________________