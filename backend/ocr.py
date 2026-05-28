import pytesseract
from PIL import Image

def extract_marks(filepath):
    text = pytesseract.image_to_string(Image.open(filepath))

    subjects = []

    if "Physics" in text:
        subjects.append("Physics")
    if "Chemistry" in text:
        subjects.append("Chemistry")
    if "Math" in text or "Mathematics" in text:
        subjects.append("Maths")
    if "Biology" in text:
        subjects.append("Biology")

    percentage = 50
    for i in range(100, 30, -1):
        if str(i) in text:
            percentage = i
            break

    return {
        "subjects": subjects,
        "percentage": percentage
    }
