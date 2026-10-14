# LAB 3: Security Policy Governance Checker
# Aim: Check whether a security policy contains the required governance elements.

policy = input("Enter security policy document: ").lower()

elements = {
    "Scope": ["scope"],
    "Roles and Responsibilities": ["roles", "responsibilities"],
    "Enforcement": ["enforcement"],
    "Review Cycle": ["review", "cycle"],
    "Approval Authority": ["approval", "authority"],
}

print("\nSecurity Policy Assessment")
for element, keywords in elements.items():
    if all(word in policy for word in keywords):
        print(element + ": Present")
    else:
        print(element + ": Missing")
