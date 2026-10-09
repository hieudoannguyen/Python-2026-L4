import math
import numpy as np


def input_students():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nStudent {i + 1}")

        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")

        student = {
            "id": student_id,
            "name": name,
            "dob": dob
        }

        students.append(student)

    return students


def input_courses():
    courses = []

    n = int(input("Enter number of courses: "))

    for i in range(n):
        print(f"\nCourse {i + 1}")

        course_id = input("Course ID: ")
        name = input("Course name: ")
        credit = float(input("Credits: "))   

        course = {
            "id": course_id,
            "name": name,
            "credit": credit              
        }

        courses.append(course)

    return courses


def input_marks(students, courses, marks):
    if len(courses) == 0:
        print("No courses available.")
        return

    list_courses(courses)

    course_id = input("\nEnter course ID: ")

    course_exists = False

    for course in courses:
        if course["id"] == course_id:
            course_exists = True
            break

    if not course_exists:
        print("Course not found.")
        return

    marks[course_id] = {}

    print(f"\nEnter marks for course: {course_id}")

    for student in students:
        mark = float(
            input(f"Mark for {student['name']} ({student['id']}): ")
        )

        mark = math.floor(mark * 10) / 10

        marks[course_id][student["id"]] = mark


def list_students(students):
    print("\n========== STUDENTS ==========")

    print(f"{'ID':<15}{'Name':<30}{'Date of Birth':<15}")
    print("-" * 60)

    for student in students:
        print(
            f"{student['id']:<15}"
            f"{student['name']:<30}"
            f"{student['dob']:<15}"
        )


def list_courses(courses):
    print("\n========== COURSES ==========")

    print(f"{'ID':<15}{'Course Name':<30}{'Credits':<10}")
    print("-" * 55)

    for course in courses:
        print(
            f"{course['id']:<15}"
            f"{course['name']:<30}"
            f"{course['credit']:<10}"
        )


def show_marks(students, courses, marks):
    list_courses(courses)

    course_id = input("\nEnter course ID: ")

    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    print(f"\n===== MARKS: {selected_course['name']} =====")

    for student in students:
        student_id = student["id"]

        if student_id in marks[course_id]:
            mark = marks[course_id][student_id]
        else:
            mark = "N/A"

        print(student_id, student["name"], mark)


def calculate_gpa(student, courses, marks):
    student_marks = []
    student_credits = []

    for course in courses:
        course_id = course["id"]

        if (
            course_id in marks
            and student["id"] in marks[course_id]
        ):
            student_marks.append(
                marks[course_id][student["id"]]
            )

            student_credits.append(
                course["credit"]
            )

    if len(student_marks) == 0:
        return 0.0

    marks_array = np.array(student_marks)
    credits_array = np.array(student_credits)

    weighted_sum = np.sum(
        marks_array * credits_array
    )

    total_credits = np.sum(credits_array)

    return weighted_sum / total_credits


def show_gpa(students, courses, marks):
    gpas = np.array([
        calculate_gpa(student, courses, marks)
        for student in students
    ])

    sorted_indices = np.argsort(gpas)[::-1]

    print("\n========== GPA ==========")

    for index in sorted_indices:
        student = students[index]

        print(
            student["id"],
            student["name"],
            round(gpas[index], 2)
        )


def main():
    students = []
    courses = []
    marks = {}

    while True:
        print("\n========== STUDENT MARK MANAGEMENT ==========")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("7. Show GPA") 
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            students = input_students()

        elif choice == "2":
            courses = input_courses()

        elif choice == "3":
            input_marks(students, courses, marks)

        elif choice == "4":
            list_students(students)

        elif choice == "5":
            list_courses(courses)

        elif choice == "6":
            show_marks(students, courses, marks)

        elif choice == "7":
            show_gpa(students, courses, marks)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()