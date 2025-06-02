from flask import Flask, render_template, request
import json
from utils.generator import generate_message

app = Flask(__name__)

# Завантаження бази уроків
with open('data/lessons.json', 'r', encoding='utf-8') as f:
    LESSONS = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form
        message = generate_message(data, LESSONS)
        return render_template("index.html", message=message, lessons=LESSONS)
    return render_template("index.html", lessons=LESSONS)

if __name__ == "__main__":
    app.run(debug=True)
