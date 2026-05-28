from flask import Flask, request, jsonify
import os
from ocr import extract_marks
from eligibility import check_eligibility

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ✅ Home route (IMPORTANT - fixes Not Found)
@app.route("/")
def home():
    return "Eligibility Checker API is Running ✅"

# ✅ Upload route
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]

    # create uploads folder if not exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    marks_data = extract_marks(filepath)
    result = check_eligibility(marks_data)

    return jsonify(result)

# ✅ Render deployment fix
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
