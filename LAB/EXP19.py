# LAB 19: Splunk-Style Search and Stats
# Aim: Filter simulated events and count results by a chosen field.

events = [
    {"host": "web-1", "sourcetype": "access", "status": "200"},
    {"host": "web-1", "sourcetype": "access", "status": "500"},
    {"host": "db-1", "sourcetype": "auth", "status": "failed"},
    {"host": "web-2", "sourcetype": "access", "status": "200"},
]

field = input("Search field (host/sourcetype/status): ").strip()
value = input("Value to search for: ").strip()
if field not in events[0]:
    print("Unknown field.")
else:
    results = [event for event in events if event[field] == value]
    print("\nMatching events:")
    for event in results:
        print(event)
    counts = {}
    for event in results:
        counts[event[field]] = counts.get(event[field], 0) + 1
    print("Stats count by", field + ":", counts)
