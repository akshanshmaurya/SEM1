students = []

while True:
    print("\nStudent Database System Menu:")
    print("1. Add new student.")
    print("2. Display student details.")
    print("3. Display average marks.")
    print("4. Display percentage of all students.")
    print("5. Display grade of a specific student.")
    print("6. Exit.")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = {
            "Subject1": float(input("Enter marks for Subject 1: ")),
            "Subject2": float(input("Enter marks for Subject 2: ")),
            "Subject3": float(input("Enter marks for Subject 3: "))
        }

        student = {
            "Name": name,
            "Roll Number": roll_number,
            "Marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        roll_number = input("Enter roll number to display student details: ")
        found_student = None

        for student in students:
            if student["Roll Number"] == roll_number:
                found_student = student
                break

        if found_student:
            print("\nStudent Details:")
            print(f"Name: {found_student['Name']}")
            print(f"Roll Number: {found_student['Roll Number']}")
            print(f"Marks: {found_student['Marks']}")
        else:
            print("Student not found!")

    elif choice == "3":
        total_marks = 0
        total_students = len(students)

        for student in students:
            total_marks += sum(student["Marks"].values())

        average_marks = total_marks / (3 * total_students)
        print(f"\nAverage Marks: {average_marks:.2f}")

    elif choice == "4":
        for student in students:
            total_marks = sum(student["Marks"].values())
            percentage = (total_marks / 3) * 100
            print(f"Roll Number: {student['Roll Number']}, Percentage: {percentage:.2f}%")

    elif choice == "5":
        roll_number = input("Enter roll number to display student grade: ")
        found_student = None

        for student in students:
            if student["Roll Number"] == roll_number:
                found_student = student
                break

        if found_student:
            total_marks = sum(found_student["Marks"].values())
            percentage = (total_marks / 3) * 100

            if percentage >= 90:
                grade = 'A'
            elif 80 <= percentage < 90:
                grade = 'B'
            elif 70 <= percentage < 80:
                grade = 'C'
            elif 60 <= percentage < 70:
                grade = 'D'
            else:
                grade = 'F'

            print(f"\nGrade for Roll Number {roll_number}: {grade}")
        else:
            print("Student not found!")

    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")