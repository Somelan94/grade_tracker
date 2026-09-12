import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "students.json")


def get_grade(score):
    if score == 100:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_feedback(score):
    if score == 100:
        return "Incredible - full marks!"
    elif score >= 90:
        return "Excellent work!"
    elif score >= 80:
        return "Great job!"
    elif score >= 70:
        return "Good effort!"
    elif score >= 60:
        return "You passed - keep improving!"
    else:
        return "Don't give up - practice makes perfect!"

def load_students():
    with open(file_path, "r") as file:
        return json.load(file)

def save_students(students):
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)
    print("Data saved")

def show_results(students):
    print("\n CLASS RESULTS")
    print("-" * 40)
    passed = 0
    failed = 0
    for student in students:
            name = student["name"]
            score = student["score"]
            grade = get_grade(score)
            feedback = get_feedback(score)
            result = "Pass" if score >= 60 else "Fail"
            if score <= 60:
                passed += 1
            else:
                failed += 1
            print(f"{name}: {score} -> Grade: {grade} | {result}")
            print(f" {feedback}")
    print("-" * 40)
    print(f"Passed: {passed} | Failed: {failed}")
    print()

def add_student(students):
    print("\n ADD STUDENT")
    name = input("Student name: ")
    while True:
        try:
            score = int(input("Enter score: "))
            if 0 <= score <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("That's not a valid number, try again.")
    students.append({"name": name, "score": score})
    print(f"{name} added with score {score}!")
    return students

def main():
    print(f"STUDENT GRADE TRACKER")
    students = load_students()

    while True:
        print("\nWhat would you like to do?")
        print("1 - View class results")
        print("2 - Add new student")
        print("3 - Save and quit")

        choice = int(input("\nEnter 1, 2 or 3!: "))

        if choice == 1:
            show_results(students)
        elif choice == 2:
            add_student(students)
        elif choice == 3:
            save_students(students)
            print("Goodbye")
            break
        else:
            print("Invalid choice, select 1, 2 or 3.")

main()