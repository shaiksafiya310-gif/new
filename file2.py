students = []

def add_student():
    students.append({
        "id": input("Enter ID: "),
        "name": input("Enter Name: "),
        "age": int(input("Enter Age: ")),
        "course": input("Enter Course: ")
    })
    print("Student Added")

def display():
    for s in students:
        print(s)

def add_marks():
    sid = input("Enter Student ID to add marks: ")
    for s in students:
        if s["id"] == sid:
            s["marks"] = {
                "Math": int(input("Math: ")),
                "Science": int(input("Science: ")),
                "English": int(input("English: ")),
                "Computer": int(input("Computer: ")),
                "History": int(input("History: "))
            }
            print("Marks added for", s["name"])
            return
    print("Student not found")

while True:
    print("\n1.Add Student\n2.Display\n3.Add Marks\n4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        display()
    elif ch == "3":
        add_marks()
    elif ch == "4":
        break
    else:
        print("Invalid Choice")