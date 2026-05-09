students = [
    {"id": "S101", "name": "Ravi Kumar", "age": 20, "course": "B.Tech"},
    {"id": "S102", "name": "Anita Sharma", "age": 22, "course": "MBA"},
    {"id": "S103", "name": "Vikram Singh", "age": 19, "course": "B.Sc"},
    {"id": "S104", "name": "Priya Mehta", "age": 21, "course": "BCA"}
]


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Student Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print(f"Student {name} added successfully!")


def display_students():
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student List ---")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")


def update_student():
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            course = input("Enter new course (leave blank to skip): ")

            if name:
                student["name"] = name
            if age:
                student["age"] = int(age)
            if course:
                student["course"] = course

            print(f"Student ID {student_id} updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print(f"Student ID {student_id} deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")