# Initialize an empty list to store product details
product_catalog = []

# Display the menu
while True:
    print("1. Add Product")
    print("2. Display Product Catalog")
    print("3. Update Product Quantity")
    print("4. Search Product by ID")
    print("5. Calculate Total Cost")
    print("6. Remove Product by ID")
    print("7. Exit")

    # Get user choice
    choice = input("Enter your choice: ")

    # Option 1: Add Product
    if choice == "1":
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        
        product = {"Product ID": product_id, "Product Name": product_name, "Quantity": quantity, "Price": price}
        product_catalog.append(product)
        print("Product added successfully!")

    # Option 2: Display Product Catalog
    elif choice == "2":
        if not product_catalog:
            print("No products in the catalog.")
        else:
            for product in product_catalog:
                print(product)

    # Option 3: Update Product Quantity
    elif choice == "3":
        product_id = input("Enter Product ID to update quantity: ")
        for product in product_catalog:
            if product["Product ID"] == product_id:
                new_quantity = int(input("Enter new quantity: "))
                product["Quantity"] = new_quantity
                print("Quantity updated successfully!")
                break
        else:
            print("Product not found.")

    # Option 4: Search Product by ID
    elif choice == "4":
        search_id = input("Enter Product ID to search: ")
        for product in product_catalog:
            if product["Product ID"] == search_id:
                print("Product found:")
                print(product)
                break
        else:
            print("Product not found.")

    # Option 5: Calculate Total Cost
    elif choice == "5":
        total_cost = sum(product["Quantity"] * product["Price"] for product in product_catalog)
        print(f"Total Cost of all products: {total_cost}")

    # Option 6: Remove Product by ID
    elif choice == "6":
        remove_id = input("Enter Product ID to remove: ")
        for product in product_catalog:
            if product["Product ID"] == remove_id:
                product_catalog.remove(product)
                print("Product removed successfully!")
                break
        else:
            print("Product not found.")

    # Option 7: Exit
    elif choice == "7":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
