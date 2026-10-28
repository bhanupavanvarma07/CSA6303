# LAB 17: ISO/IEC 27001 Annex A Domain Classifier
# Aim: Map a described security control to a broad Annex A domain.

description = input("Describe the security control: ").lower()
domains = {
    "Organizational controls": ["policy", "supplier", "governance", "incident management"],
    "People controls": ["employee", "awareness", "training", "screening"],
    "Physical controls": ["building", "door", "visitor", "equipment"],
    "Technological controls": ["encryption", "firewall", "access control", "logging", "backup"],
}

matches = [
    domain for domain, keywords in domains.items()
    if any(keyword in description for keyword in keywords)
]
if matches:
    print("Likely Annex A domain:", ", ".join(matches))
else:
    print("Domain not identified; consult the current ISO/IEC 27001 control set.")
