def products_menu():
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
            for i, product in enumerate(products_list):
                print(f"{i}: {product['name']}-£{product['Price']:.2f}")
        elif choice == "2":
            name = input("Enter Product Name: ")
            price = float(input("What is the price of the product? "))
            products_list.append ({"name":name, "Price":price})
            print(f"New Product '{name}' added.")
        elif choice == "3":
            product_delete = input("What product do you want deleted?: ")
            for product in products_list:
                if product['name']==product_delete:
                    products_list.remove(product)
                    print(f"{product['name']} deleted. ")
        elif choice == "4":
            idx = int(input("\nEnter the index of the product you want to update: \n"))
            if 0 <= idx < len(products_list):
                new_name = input("\nWhat is the new name of the product you would like to update? \n")
                new_price = (float(input("\nWhat is the new price of this product? \n")))
                products_list[idx] = ({"name":new_name, "Price":new_price})
                print("\nProduct updated! \n")
        elif choice == "0":
            main_menu()
        else:
            print("Invalid choice, please try again :)")
            break