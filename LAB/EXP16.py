# LAB 16: Defense-in-Depth Simulation
# Aim: Show how multiple independent controls can stop an attack.

attack = input("Enter attack type (phishing/malware/unknown): ").strip().lower()
layers = [
    ("Email filter", attack == "phishing"),
    ("Endpoint protection", attack == "malware"),
    ("Network monitoring", attack in {"phishing", "malware"}),
    ("Access control", attack != "unknown"),
]

blocked = False
for layer, detects_attack in layers:
    if detects_attack:
        print(layer + ": BLOCKED the attack")
        blocked = True
        break
    print(layer + ": No match; attack continues")

if not blocked:
    print("Attack passed the modeled controls. Review and improve the defense layers.")
