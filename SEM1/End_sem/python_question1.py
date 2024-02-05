# Initialize an empty list to store vehicle entries
vehicle_entries = []

# Display the menu
while True:
    print("1. Add Vehicle Entry")
    print("2. Display Vehicle Entries")
    print("3. Calculate Total Toll Collection")
    print("4. Search Vehicle by Number")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice: ")

    # Option 1: Add Vehicle Entry
    if choice == "1":
        vehicle_number = input("Enter Vehicle Number: ")
        vehicle_type = input("Enter Vehicle Type (Car/Truck/Bus): ")
        toll_amount = float(input("Enter Toll Amount: "))
        
        entry = {"Vehicle Number": vehicle_number, "Vehicle Type": vehicle_type, "Toll Amount": toll_amount}
        vehicle_entries.append(entry)
        print("Vehicle entry added successfully!")

    # Option 2: Display Vehicle Entries
    elif choice == "2":
        if not vehicle_entries:
            print("No vehicles on the bridge.")
        else:
            for entry in vehicle_entries:
                print(entry)

    # Option 3: Calculate Total Toll Collection
    elif choice == "3":
        total_toll = sum(entry["Toll Amount"] for entry in vehicle_entries)
        print(f"Total Toll Collection: {total_toll}")

    # Option 4: Search Vehicle by Number
    elif choice == "4":
        search_number = input("Enter Vehicle Number to search: ")
        found_entries = [entry for entry in vehicle_entries if entry["Vehicle Number"] == search_number]
        
        if found_entries:
            print("Vehicle found:")
            for entry in found_entries:
                print(entry)
        else:
            print("Vehicle not found.")

    # Option 5: Exit
    elif choice == "5":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
