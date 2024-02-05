def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Student Course: ")
    student = {'id': id, 'name': name, 'age': age, 'course': course}
    students.append(student)
    print("\nStudent Admitted Successfully!")

def display_students():
    if len(students) == 0:
        print("\nNo Students Admitted Yet!")
    else:
        print("\nStudent Details:")
        print("==================")
        for student in students:
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print("\n------------------\n")

def update_student():
    id = input("Enter Student ID: ")
    for student in students:
        if student['id'] == id:
            print("\nAvailable Details to Update:")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("\n0. Back to Main Menu")
            choice = int(input("Enter Choice (0-3): "))
            if choice == 1:
                name = input("Enter Updated Name: ")
                student['name'] = name
            elif choice == 2:
                age = int(input("Enter Updated Age: "))
                student['age'] = age
            elif choice == 3:
                course = input("Enter Updated Course: ")
                student['course'] = course
            else:
                break
            print("\nStudent Details Updated Successfully!")
            break
    else:
        print("\nNo Student Found with the Given ID!")

def search_student():
    id = input("Enter Student ID: ")
    for student in students:
        if student['id'] == id:
            print("\nStudent Details:")
            print("==================")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print("\n------------------\n")
            break
    else:
        print("\nNo Student Found with the Given ID!")

def calculate_average_age():
    if len(students) == 0:
        print("\nNo Students Admitted Yet!")
    else:
        total_age = sum([student['age'] for student in students])
        average_age = total_age / len(students)
        print(f"\nAverage Age of Admitted Students: {average_age}")

def remove_student():
    id = input("Enter Student ID: ")
    for student in students:
        if student['id'] == id:
            students.remove(student)
            print("\nStudent Removed Successfully!")
            break
    else:
        print("\nNo Student Found with the Given ID!")

students = []

while True:
    print("\nStudent Admission Process Management System")
    print("==========================================")
    print("1. Admit Student")
    print("2. Display Student List")
    print("3. Update Student Information")
    print("4. Search Student by ID")
    print("5. Calculate Average Age")
    print("6. Remove Student by ID")
    print("7. Exit")
    print("\n0. Back to Main Menu")
    choice = int(input("Enter Choice (0-7): "))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        search_student()
    elif choice == 5:
        calculate_average_age()
    elif choice == 6:
        remove_student()
    elif choice == 7:
        print("\nThank You for Using the System")
        break