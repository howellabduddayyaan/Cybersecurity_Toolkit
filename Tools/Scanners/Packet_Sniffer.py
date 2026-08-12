# ======================
# === Packet Sniffer ===
# ======================

from scapy.all import sniff, IP, TCP, UDP, ICMP

from shared.banner import show_banner
from shared.tables import print_section, print_analysis_complete


# _________________________________________________________________________________________________

packet_count = 0

def sniff_packet(packet):

    global packet_count

    packet_count += 1

    print("\n")
    print("=" * 60)
    print(f"Packet {packet_count}")
    print("=" * 60)

    # _____________________________________________________________________________________________

