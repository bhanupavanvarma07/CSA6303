# LAB 1: Threat Intelligence Application Area
# Aim: Identify the relevant threat-intelligence application area based on a business scenario.

scenario = input("Enter business scenario: ").lower()

if "bank" in scenario or "fraud" in scenario:
    print("Application Area: Banking Fraud Prevention")
elif "hospital" in scenario or "healthcare" in scenario:
    print("Application Area: Healthcare Data Protection")
elif "shopping" in scenario or "e-commerce" in scenario:
    print("Application Area: E-commerce Fraud Prevention")
else:
    print("Application Area: General Threat Intelligence")
