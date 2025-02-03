
# Define an empty list to hold products
products_list = []

# Load products from a text file
def load_products():
        with open("products.txt", "r") as file:
            for line in file:
                name, price = line.strip().split(",")
                products_list.append({"name": name, "Price": float(price)})

# Save products to a text file
def save_products():
    with open("products.txt", "w") as file:
        for product in products_list:
            file.write(f"{product['name']},{product['Price']}\n")

 
def products_menu():
    load_products()
    while True:
        print("\nProducts Menu")
        print("1. View Products")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Update Product")
        print("0. Back to Main Menu")
        choice = input("Choose an option: \n")

        if choice == "1":
            print("\nProducts")
            print("\nChoose an item:")
            for i, product in enumerate(products_list, start=1):
                print(f"{i}: {product['name']}-£{product['Price']:.2f}")

        elif choice == "2":
            name = input("Enter Product Name: ")
            price = float(input("What is the price of the product? "))
            products_list.append ({"name":name, "Price":price})
            print(f"New Product '{name}' added.")
            save_products()

        elif choice == "3":
            for i, product in enumerate(products_list, start=1):
                print(f"{i}: {product['name']}-£{product['Price']:.2f}")
            index = int(input("Which product do you want to delete: ")) - 1
            del products_list[index]
            print(f"{product['name']} deleted. ")
            save_products()

        elif choice == "4":
            for i, product in enumerate(products_list, start=1):
                print(f"{i}: {product['name']}-£{product['Price']:.2f}")
            idx = int(input("\nEnter the index of the product you want to update: \n")) - 1
            
            if 0 <= idx < len(products_list):
                new_name = input(f"\nWhat is the new name of the product you would like to update? (Leave blank to keep {product['name']}) \n")
                if not new_name:
                    new_name = product['name']  # Keep the existing name if blank
    
                new_price_input = input(f"\nWhat is the new price of this product? (Leave blank to keep {product['Price']}) \n")
                try:
                    new_price = float(new_price_input) if new_price_input else product['Price']  # Keep existing price if blank
                except ValueError:
                    print("\nInvalid input, Price must be a number.")
                    return  # Exit the function to let the user try again

                # Update the product in the list
                products_list[idx] = {"name": new_name, "Price": new_price}
                print("\nProduct updated! \n")
                save_products()

        elif choice == "0":
            print("\nSaving changes...")
            print("Data saved successfully!\n")
            break
        else:
            print("Invalid choice, please try again :)")