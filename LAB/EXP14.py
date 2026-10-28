# LAB 14: SIEM Pipeline Demonstration
# Aim: Collect, normalize, correlate events, and raise an alert.

raw_events = [
    {"source": "firewall", "src_ip": "198.51.100.7", "event": "connection_denied"},
    {"source": "endpoint", "src_ip": "198.51.100.7", "event": "malware_detected"},
    {"source": "identity", "src_ip": "203.0.113.8", "event": "login_success"},
]

# Normalize fields into a common event schema.
events = [
    {
        "source": item["source"].lower(),
        "ip": item["src_ip"],
        "event_type": item["event"].lower(),
    }
    for item in raw_events
]

# Correlate events by IP address and alert when both indicators occur.
events_by_ip = {}
for event in events:
    events_by_ip.setdefault(event["ip"], set()).add(event["event_type"])

print("Normalized events:", events)
for ip, event_types in events_by_ip.items():
    if {"connection_denied", "malware_detected"}.issubset(event_types):
        print("SIEM ALERT: Firewall block and malware detection observed for", ip)
