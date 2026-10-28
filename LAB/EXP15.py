# LAB 15: Security Incident Root-Cause Classifier
# Aim: Classify a case-study narrative by its likely root cause.

narrative = input("Enter incident case-study narrative: ").lower()
categories = {
    "Phishing": ["phishing", "email link", "credential theft", "fake login"],
    "Unpatched vulnerability": ["unpatched", "missing patch", "known vulnerability", "outdated software"],
    "Misconfiguration": ["misconfigured", "publicly exposed", "default password", "open storage"],
    "Insider threat": ["insider", "employee copied", "staff member", "unauthorized employee"],
    "Supply-chain compromise": ["supplier", "vendor", "third-party update", "supply chain"],
}

scores = {
    category: sum(keyword in narrative for keyword in keywords)
    for category, keywords in categories.items()
}
best_score = max(scores.values())
if best_score == 0:
    print("Root cause: Unable to classify")
else:
    likely_causes = [category for category, score in scores.items() if score == best_score]
    print("Likely root-cause category:", ", ".join(likely_causes))
