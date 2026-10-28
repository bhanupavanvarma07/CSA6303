# LAB 9: Threat Intelligence Lifecycle Stage Tagger
# Aim: Match an intelligence-team activity to a lifecycle stage using keywords.

activity = input("Describe the intelligence team activity: ").lower()
stages = {
    "Direction": ["requirement", "priority", "objective", "question"],
    "Collection": ["collect", "gather", "source", "feed"],
    "Processing": ["normalize", "clean", "filter", "format"],
    "Analysis": ["analyze", "assess", "correlate", "interpret"],
    "Dissemination": ["share", "distribute", "report", "brief"],
    "Feedback": ["feedback", "review", "improve", "refine"],
}

matches = [stage for stage, words in stages.items() if any(word in activity for word in words)]
if matches:
    print("Likely lifecycle stage:", ", ".join(matches))
else:
    print("Stage could not be identified from the description.")
