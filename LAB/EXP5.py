# LAB 5: Threat Intelligence Report Classification
# Aim: Classify a threat-intelligence report as Strategic, Tactical, or Operational.

report = input("Enter threat intelligence report description: ").lower()

if any(word in report for word in ["business impact", "long-term", "executive", "industry trend"]):
    print("Report Type: Strategic")
elif any(word in report for word in ["attack technique", "tactics", "mitre", "ttp"]):
    print("Report Type: Tactical")
elif any(word in report for word in ["ip address", "malicious domain", "hash", "active attack"]):
    print("Report Type: Operational")
else:
    print("Report Type: Unable to classify")
