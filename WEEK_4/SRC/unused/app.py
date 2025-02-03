products_list = [{"name":"Wireless Bluetooth Speaker", "Price": 19.99},
                 {"name":"Microphone","Price":15.99},
                 {"name":"Graphing Calculator","Price":34.99},
                 {"name":"Ring Light","Price":5.99} ,
                 {"name":"Keyboard","Price":10.99},
                 {"name":"Webcam","Price":11.99},
                 {"name":"Noise cancelling Headphones","Price":54.99},
                 {"name":"Powerbank Phone Charger","Price":20.00},
                 {"name":"Phone Charger Adapter", "Price":6.99},
                 {"name":"Blue Light Glasses","Price":11.99}
                 ]

couriers_list = [{"name":"Amazon","Delivery Fee":3.99},
                 {"name":"Royal Mail Next Day Delivery","Delivery Fee":7.99},
                 {"name":"Royal Mail","Delivery Fee":4.99},
                 {"name":"Hermes","Delivery Fee":1.99}
]

# Main menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Products")
        print("2. Orders")
        print("3. Couriers")
        print("0. Exit")
        choice = input("Choose an option: \n")
        if choice == "1":
            products_menu()
        elif choice == "2":
            order_menu()
        elif choice == "3":
            courier_menu()
        elif choice == "0":
            main_menu()
            print("Thanks for stopping by!\n")
            break
        else:
            print("Invalid choice, please try again :)\n")

# Products menu
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

# Courier menu (add more menu options: View courier, update courier, back to main menu)
def courier_menu():

    print("\nPick a courier here: ")
    while True:
        print("1. Amazon")
        print("2. Royal Mail Next Day Delivery")
        print("3. Royal Mail")
        print("4. Hermes")
        print("0. Main Menu")
        choice = input("Choose your courier: ")

        if choice == "1":
            print("\nCourier selected:")
            for i, courier in enumerate(couriers_list):
                print(f"{i}:{courier['name']}")
                print("\nThat will cost: ")
                print(f"{i}:£{courier['Delivery Fee']:.2f}")
        elif choice == "2":
            print("\nCourier selected:")
            for i, courier in enumerate(couriers_list):
                print(f"{i}:{courier['name']}")
                print("\nThat will cost: ")
                print(f"{i}:£{courier['Delivery Fee']:.2f}")
        elif choice == "3":
            print("\nCourier selected:")
            for i, courier in enumerate(couriers_list):
                print(f"{i}:{courier['name']}")
                print("\nThat will cost: ")
                print(f"{i}:£{courier['Delivery Fee']:.2f}")
        elif choice == "4":
            print("\nCourier selected:")
            for i, courier in enumerate(couriers_list):
                print(f"{i}:{courier['name']}")
                print("\nThat will cost: ")
                print(f"{i}:£{courier['Delivery Fee']:.2f}")
        elif choice == "0":
            main_menu()
        else:
            print("Invalid choice, please try again :)")
            i += 1

# Orders directory and statuses
orders_list = [{"customer_name":"customer one","customer_address":"19 Amberly Rd", "phone_number":"07940134452","status":"Preparing"},
          {"customer_name":"customer two","customer_address":"3 Moon Rd", "phone_number":"07540977851","status":"Preparing"},
          {"customer_name":"customer three","customer_address":"62 Brolic Rd", "phone_number":"07921237687","status":"Out For Delivery"}
          ]

current_status = ["Preparing","Out For Delivery","Delivered"]

# Order Menu
def order_menu():
    while True:
        print("\n Orders Menu\n")
        print("1. View All Orders")
        print("2. New Order")
        print("3. Update Order Status")
        print("4. Update Order Details")
        print("5. Delete An Order")
        print("0. Return to main menu")
        choice = input("Choose an option: \n")

        if choice == "1":
            print("\n All current orders\n")
            for idx, order in enumerate(orders_list):
                print(f"{idx}: {order}")
        elif choice == "2":
            customer_name = (input("Enter New Customers Name Here: "))
            customer_address = (input("Enter New Customer Address Here: "))
            phone_number = (input("Enter New Customers Phone Number Here: "))
            new_order = {"customer_name": customer_name,
            "customer_address":customer_address,
            "phone_number":phone_number,
            "status":"Preparing"}
            
            orders_list.append(new_order)
            print(f"\nNew order for {customer_name} created\n")
        elif choice == "3":
            print("\nOrders list: \n")
            for idx, order in enumerate(orders_list):
                print(f"Order {idx}:{order}")
            try:
                orders_index = int(input("\nWhat is the index of the order you would like to update? \n"))
                if 0 <= orders_index < len(orders_list):
                        print("Status Options")
                        for idx, status in enumerate(current_status):
                            print(f"{idx}:{status}")
                        status_index = int(input("\nWhat is the index of the status you wish to update to?\n"))
                        if 0 <= status_index < len(current_status):
                            order[orders_index]['status'] = current_status[status_index]
                            print("\nOrder status for {orders_index} has been updated to {current_status[status_index]}")
                        else:
                            print("\nInvalid status index\n")
                else:
                    print("\nInvalid Order Index\n")                
            except:
                ValueError 
                print("\nEnter a valid number\n")
        elif choice == "4":
            print("\nTime to update an Order!\n")
            for idx, order in enumerate(orders_list):
                print(f'Order {idx}:{order}')
            try:
                orders_index = int(input("\nWhat order are you updating? \n"))
                if 0 <= orders_index < len(orders_list):
                    order_selection = orders_list[orders_index]
                    for key,value in order_selection.items():
                        new_value = input(f"Updating {key}:{value}")
                        if new_value:
                            order_selection[key]=new_value
                    print(f"\nOrder {orders_index} updated successfully\n")
                else:
                    print("Invalid order index")
            except ValueError:
                print("\nEnter a valid number\n")
        elif choice == "5":
            print("\nOrders list: \n")
            for idx,order in enumerate(orders_list):
                print(f"Order {idx}:{order}")
            try:
                orders_index = int(input("\nWhat order are you deleting? \n"))
                if 0 <= orders_index < len(orders_list):
                    deleted_order = orders_list.pop(orders_index)
                    print(f"\nOrder {deleted_order} deleted successfully")
                else:
                    print("\nInvalid choice, please choose again\n")
            except ValueError:
                print("\nInvalid number entered\n")
        else:
            if choice == "0":
                main_menu()
            
main_menu()
