
student_list = []
while True:
    print("1. Admit Student")
    print("2. Display Student List")
    print("3. Update Student Information")
    print("4. Search Student by ID")
    print("5. Calculate Average Age")
    print("6. Remove Student by ID")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        
        student = {"Student ID": student_id, "Name": name, "Age": age, "Course": course}
        student_list.append(student)
        print("Student admitted successfully!")

    elif choice == "2":
        if not student_list:
            print("No students admitted.")
        else:
            for student in student_list:
                print(student)

    elif choice == "3":
        student_id = input("Enter Student ID to update information: ")
        for student in student_list:
            if student["Student ID"] == student_id:
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Course")
                update_choice = input("Enter your update choice: ")
                
                if update_choice == "1":
                    new_name = input("Enter new Name: ")
                    student["Name"] = new_name
                    print("Name updated successfully!")
                elif update_choice == "2":
                    new_age = int(input("Enter new Age: "))
                    student["Age"] = new_age
                    print("Age updated successfully!")
                elif update_choice == "3":
                    new_course = input("Enter new Course: ")
                    student["Course"] = new_course
                    print("Course updated successfully!")
                else:
                    print("Invalid update choice.")
                break
        else:
            print("Student not found.")

    elif choice == "4":
        search_id = input("Enter Student ID to search: ")
        for student in student_list:
            if student["Student ID"] == search_id:
                print("Student found:")
                print(student)
                break
        else:
            print("Student not found.")

    elif choice == "5":
        if not student_list:
            print("No students admitted.")
        else:
            total_age = sum(student["Age"] for student in student_list)
            average_age = total_age / len(student_list)
            print(f"Average Age of admitted students: {average_age}")

    elif choice == "6":
        remove_id = input("Enter Student ID to remove: ")
        for student in student_list:
            if student["Student ID"] == remove_id:
                student_list.remove(student)
                print("Student removed successfully!")
                break
        else:
            print("Student not found.")

    elif choice == "7":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
