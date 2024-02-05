# Initialize an empty list to store medicine details
medicine_inventory = {}

# Display the menu
while True:
    print("1. Add Medicine")
    print("2. Display Medicine Inventory")
    print("3. Update Medicine Quantity")
    print("4. Search Medicine by ID")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice: ")

    # Option 1: Add Medicine
    if choice == "1":
        medicine_id = input("Enter Medicine ID: ")
        medicine_name = input("Enter Medicine Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        
        medicine = {
            "Medicine ID": medicine_id,
            "Medicine Name": medicine_name, 
            "Quantity": quantity, 
            "Price": price
            }
        medicine_inventory.update(medicine)
        print("Medicine added successfully!")

    # Option 2: Display Medicine Inventory
    elif choice == "2":
        if not medicine_inventory:
            print("No medicines in the inventory.")
        else:
            for a,b in medicine_inventory.items():
                print(a ,":", b)

    # Option 3: Update Medicine Quantity
    elif choice == "3":
        medicine_id = input("Enter Medicine ID to update quantity: ")
        for medicine in medicine_inventory:
            if medicine["Medicine ID"] == medicine_id:
                new_quantity = int(input("Enter new quantity: "))
                medicine["Quantity"] = new_quantity
                print("Quantity updated successfully!")
                break
        else:
            print("Medicine not found.")

    # Option 4: Search Medicine by ID
    elif choice == "4":
        search_id = input("Enter Medicine ID to search: ")
        for medicine in medicine_inventory:
            if medicine["Medicine ID"] == search_id:
                print("Medicine found:")
                print(medicine)
                break
        else:
            print("Medicine not found.")

    # Option 5: Exit
    elif choice == "5":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
