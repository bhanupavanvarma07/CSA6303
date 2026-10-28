# LAB 13: Threat Intelligence Qualification
# Aim: Determine whether collected data has context, confidence, and actionability.

context = input("Does the data include threat context? (yes/no): ").strip().lower()
confidence = input("Confidence level (low/medium/high): ").strip().lower()
actionable = input("Can defenders take a specific action? (yes/no): ").strip().lower()

has_context = context == "yes"
has_confidence = confidence in {"low", "medium", "high"}
has_action = actionable == "yes"

if has_context and has_confidence and has_action:
    print("Assessment: Threat intelligence")
    print("Context:", "Present")
    print("Confidence:", confidence.title())
    print("Actionability: Present")
else:
    print("Assessment: Unprocessed or incomplete raw data")
    print("A useful intelligence item needs context, a valid confidence assessment, and an action.")
