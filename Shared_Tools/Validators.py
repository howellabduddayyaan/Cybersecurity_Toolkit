# ==================
# === Validators ===
# ==================

import socket

def valid_ip(ip):

    try:
        socket.inet_aton(ip)
        return True

    except socket.error:
        return False


def valid_port(port):
    return 1 <= port <= 65535

# _________________________________________________________________________________________________