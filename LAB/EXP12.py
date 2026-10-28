# LAB 12: SOC Alert Priority Triage
# Aim: Assign a P1-P4 priority based on alert description keywords.

description = input("Enter SOC alert description: ").lower()
priority_keywords = {
    "P1 - Critical": ["ransomware", "data exfiltration", "domain controller", "active breach"],
    "P2 - High": ["privilege escalation", "malware", "multiple failed logins", "critical server"],
    "P3 - Medium": ["suspicious login", "policy violation", "unusual process"],
    "P4 - Low": ["informational", "known scanner", "low risk"],
}

for priority, keywords in priority_keywords.items():
    if any(keyword in description for keyword in keywords):
        print("Alert Priority:", priority)
        break
else:
    print("Alert Priority: P3 - Medium (manual review recommended)")
