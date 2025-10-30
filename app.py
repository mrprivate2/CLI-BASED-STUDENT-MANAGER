from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

students = []  # Temporary in-memory data (can be extended to DB later)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_student():
    data = request.get_json()
    name = data.get("name")
    roll = data.get("roll")
    course = data.get("course")

    if any(s["roll"] == roll for s in students):
        return jsonify({"error": "Roll number already exists!"}), 400

    students.append({"name": name, "roll": roll, "course": course})
    return jsonify({"message": "Student added successfully!", "students": students})

@app.route("/get", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/search/<roll>", methods=["GET"])
def search_student(roll):
    for student in students:
        if student["roll"] == roll:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

@app.route("/delete/<roll>", methods=["DELETE"])
def delete_student(roll):
    global students
    students = [s for s in students if s["roll"] != roll]
    return jsonify({"message": "Deleted successfully!", "students": students})

if __name__ == "__main__":
    app.run(debug=True)
