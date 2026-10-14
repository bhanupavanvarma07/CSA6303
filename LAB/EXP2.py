# LAB 2: Simple Port Scanner
# Aim: Identify open ports on a target host.

import socket

host = input("Enter target host (use localhost for practice): ")
ports = [22, 80, 443, 3306, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED or FILTERED")
    s.close()
