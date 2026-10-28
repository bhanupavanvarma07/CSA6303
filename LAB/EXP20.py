# LAB 20: Network Threat Category Classifier
# Aim: Classify an incident description as Phishing, DoS/DDoS, Malware, or Man-in-the-Middle.

description = input("Enter incident description: ").lower()
categories = {
    "Phishing": ["phishing", "fake email", "credential", "deceptive link"],
    "DoS/DDoS": ["denial of service", "ddos", "flood of requests", "service outage"],
    "Malware": ["malware", "ransomware", "trojan", "infected file"],
    "Man-in-the-Middle": ["man-in-the-middle", "mitm", "intercepted traffic", "rogue access point"],
}

matches = [
    category for category, keywords in categories.items()
    if any(keyword in description for keyword in keywords)
]
if matches:
    print("Threat category:", ", ".join(matches))
else:
    print("Threat category: Unable to classify")
