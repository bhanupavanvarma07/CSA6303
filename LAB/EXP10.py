# LAB 10: Stateful Inspection Firewall Simulation
# Aim: Permit return traffic for tracked outbound connections and block unsolicited inbound traffic.

connection_table = set()
print("Commands: outbound <source> <destination> <port>")
print("          inbound <source> <destination> <port>")
print("          quit")

while True:
    parts = input("Packet> ").strip().lower().split()
    if not parts or parts[0] == "quit":
        break
    if len(parts) != 4 or parts[0] not in {"outbound", "inbound"}:
        print("Enter a valid command with direction, source, destination, and port.")
        continue

    direction, source, destination, port = parts
    if direction == "outbound":
        connection_table.add((source, destination, port))
        print("ALLOWED: outbound connection recorded")
    elif (destination, source, port) in connection_table:
        print("ALLOWED: return traffic matches a tracked connection")
    else:
        print("BLOCKED: unsolicited inbound traffic")
