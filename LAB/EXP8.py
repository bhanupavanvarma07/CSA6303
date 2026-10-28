# LAB 8: Network Segmentation and Lateral Movement
# Aim: Demonstrate that a low-trust segment cannot access a sensitive segment.

access_policy = {
    "low_trust": ["internet", "shared_services"],
    "user": ["internet", "shared_services"],
    "sensitive": ["shared_services"],
}

source = input("Enter source segment (low_trust/user/sensitive): ").strip().lower()
destination = input("Enter destination segment (internet/shared_services/sensitive): ").strip().lower()

if source not in access_policy:
    print("Unknown source segment.")
elif destination not in {"internet", "shared_services", "sensitive"}:
    print("Unknown destination segment.")
elif destination in access_policy[source]:
    print("ACCESS ALLOWED:", source, "->", destination)
else:
    print("ACCESS BLOCKED by segmentation policy:", source, "->", destination)
    print("Lateral movement into this segment is prevented.")
