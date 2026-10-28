# LAB 11: Packet Sniffing with Scapy
# Aim: Display summaries of packets captured on an authorized interface.
# Run only on a network you own or have permission to monitor.

from scapy.all import sniff

interface = input("Enter interface name (for example, en0): ").strip()
packet_count = int(input("Number of packets to capture: "))

if packet_count <= 0:
    raise ValueError("Packet count must be greater than zero.")

print("Capturing", packet_count, "packets on", interface)
packets = sniff(iface=interface, count=packet_count, prn=lambda packet: print(packet.summary()))
print("Capture complete. Packets captured:", len(packets))
