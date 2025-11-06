import json
import os

FILENAME = "students.json"


# ---------------- Utility Functions ---------------- #

def load_students():
    """Load student data from file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_students(students):
    """Save student data to file."""
    with open(FILENAME, "w") as f:
        json.dump(students, f, indent=4)


# ---------------- CRUD Operations ---------------- #

def add_student():
    """Add a new student."""
    students = load_students()
    roll = input("Enter Roll Number: ")

    # Check for duplicate roll number
    if any(s["roll"] == roll for s in students):
        print(" Roll number already exists!")
        return

    name = input("Enter Name: ")
    course = input("Enter Course: ")

    students.append({"roll": roll, "name": name, "course": course})
    save_students(students)
    print(" Student added successfully!")


def view_students():
    """Display all students."""
    students = load_students()
    if not students:
        print(" No students found!")
        return
    print("\n List of Students:")
    print("-" * 40)
    for s in students:
        print(f"Roll: {s['roll']}\tName: {s['name']}\tCourse: {s['course']}")
    print("-" * 40)


def search_student():
    """Search for a student by roll number."""
    students = load_students()
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"\n Student Found!\nRoll: {s['roll']}\nName: {s['name']}\nCourse: {s['course']}")
            return
    print("Student not found!")


def delete_student():
    """Delete a student by roll number."""
    students = load_students()
    roll = input("Enter Roll Number to Delete: ")

    new_students = [s for s in students if s["roll"] != roll]
    if len(new_students) == len(students):
        print(" Student not found!")
    else:
        save_students(new_students)
        print(" Student deleted successfully!")


def modify_student():
    """Modify existing student details."""
    students = load_students()
    roll = input("Enter Roll Number to Modify: ")

    for s in students:
        if s["roll"] == roll:
            print(f"Current Details: {s}")
            name = input("Enter New Name (leave blank to keep same): ")
            course = input("Enter New Course (leave blank to keep same): ")

            if name.strip():
                s["name"] = name
            if course.strip():
                s["course"] = course

            save_students(students)
            print("Student details updated!")
            return

    print("Student not found!")


# ---------------- Menu System ---------------- #

def menu():
    while True:
        print("\n===== 🎓 STUDENT MANAGEMENT CLI =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Modify Student")
        print("5. Delete Student")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            modify_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1-6.")


# ---------------- Run the CLI ---------------- #
if __name__ == "__main__":
    menu()1
    