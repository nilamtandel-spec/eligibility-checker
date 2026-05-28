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
    if "60" in text:
        percentage = 60

    return {
        "subjects": subjects,
        "percentage": percentage
    }
