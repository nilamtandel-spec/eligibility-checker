def check_eligibility(data):
    subjects = data["subjects"]
    percentage = data["percentage"]

    eligible = []
    not_eligible = []

    if percentage >= 45 and all(sub in subjects for sub in ["Physics", "Chemistry", "Maths"]):
        eligible.append("B.Tech")
    else:
        not_eligible.append("B.Tech (PCM required, 45%)")

    if percentage >= 45 and ("Biology" in subjects or "Maths" in subjects):
        eligible.append("Pharmacy")
    else:
        not_eligible.append("Pharmacy (PCB/PCM required)")

    if percentage >= 40:
        eligible.append("BCA")
    else:
        not_eligible.append("BCA (40% required)")

    return {
        "eligible": eligible,
        "not_eligible": not_eligible
    }
