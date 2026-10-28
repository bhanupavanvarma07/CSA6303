# LAB 7: ELK Stack Roles Demonstration
# Aim: Simulate Logstash parsing, Elasticsearch-style indexing, and Kibana-style aggregation.

raw_logs = [
    "2026-10-14T10:00:00Z auth user=alex status=failed src=192.0.2.10",
    "2026-10-14T10:01:00Z auth user=alex status=success src=192.0.2.10",
    "2026-10-14T10:02:00Z web user=sam status=success src=192.0.2.20",
]

# Logstash-style parsing into structured events.
events = []
for line in raw_logs:
    parts = line.split()
    event = {"timestamp": parts[0], "event_type": parts[1]}
    for item in parts[2:]:
        key, value = item.split("=", 1)
        event[key] = value
    events.append(event)

# Elasticsearch-style indexing: use an in-memory dictionary keyed by event ID.
index = {str(number): event for number, event in enumerate(events, start=1)}

# Kibana-style aggregation: count events grouped by type and status.
counts = {}
for event in index.values():
    key = (event["event_type"], event.get("status", "unknown"))
    counts[key] = counts.get(key, 0) + 1

print("Indexed events:")
for event_id, event in index.items():
    print(event_id, event)
print("\nEvent counts by type and status:")
for (event_type, status), count in counts.items():
    print(event_type, status + ":", count)
