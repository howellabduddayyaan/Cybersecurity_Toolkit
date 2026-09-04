# ======================
# === Packet Sniffer ===
# ======================

from scapy.all import sniff, IP, TCP, UDP, ICMP

from Shared_Tools.Banner import show_banner
from Shared_Tools.Tables import print_section, print_analysis_complete

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

    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print_section(
            "IP Information",
            {
                "Source IP": source_ip,
                "Destination IP": destination_ip
            }
        )

        # _________________________________________________________________________________________

        if TCP in packet:

            print_section(
                "TCP Information",
                {
                    "Protocol": "TCP",
                    "Source Port": packet[TCP].sport,
                    "Destination Port": packet[TCP].dport
                }
            )

        # _________________________________________________________________________________________

        elif UDP in packet:

            print_section(
                "UDP Information",
                {
                    "Protocol": "UDP",
                    "Source Port": packet[UDP].sport,
                    "Destination Port": packet[UDP].dport
                }
            )

        # _________________________________________________________________________________________

        elif ICMP in packet:

            print_section(
                "ICMP Information",
                {
                    "Protocol": "ICMP"
                }
            )

        # _________________________________________________________________________________________

        else:

            print_section(
                "Protocol Information",
                {
                    "Protocol": "Other"
                }
            )

    else:

        print_section(
            "Packet Information",
            {
                "Protocol": "Non-IP"
            }
        )

# _________________________________________________________________________________________________

def main():

    show_banner("Packet Sniffer")

    print("\nListening for packets...")
    print("Press CTRL+C to stop.\n")

    try:

        sniff(
            prn=sniff_packet,
            store=False
        )

    except KeyboardInterrupt:

        print("\n\nPacket Sniffer Stopped.")

        print_section(
            "Capture Summary",
            {
                "Packets Captured": packet_count
            }
        )
        
        analysis_complete = "Analysis Complete"
        
        print_analysis_complete(analysis_complete)

if __name__ == "__main__":
    main()
    
# _________________________________________________________________________________________________