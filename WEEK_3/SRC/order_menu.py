def orders_menu():
    while True:
        print("\n Orders Menu\n")
        print("1. View All Orders")
        print("2. Add New Order")
        print("3. Update Order Status")
        print("4. Update Order Details")
        print("5. Delete An Order")
        print("0. Return to main menu")
        choice = input("Choose an option: \n")

        if choice == "1":
            print("\n All current orders\n")
            for idx, order in enumerate(orders):
                print(f"{idx}: {order}")
        elif choice == "2":
            customer_name = (input("Enter New Customers Name Here: "))
            customer_address = (input("Enter New Customer Address Here: "))
            phone_number = (input("Enter New Customers Phone Number Here: "))
            new_order = {"customer_name": customer_name,
            "customer_address":customer_address,
            "phone_number":phone_number}
            print("\nCouriers Available: \n")

            for idx,order in enumerate(couriers):
                print(f"{idx}:{courier}")
            courier_index = int(input("\nWhich courier would you like?\n"))
            new_order = {
                'customer_name':customer_name,
                'customer_address':customer_address,
                'phone_number':phone_number,
                'courier':couriers[courier_index],
                'order_status':'Preparing'
            }
            orders.append(new_order)
            print(f"\nNew order for {customer_name} created\n")

        elif choice == "3":
            print("\nAll Current Orders:\n")
            for idx,order in enumerate(orders):
                print(f"{idx}:{order}")
            order_index = int(input("\nWhat is the index of the order you would like to change?"))
            print("\nOrder statues: ")
            for idx, status in enumerate(order_status):
                print(f"{i}:{status}")
            status_index = int(input("\nEnter the index of the you would like to update this order with: "))
            orders[order_index]['status'] = order_status[status_index]
            print(f"Order status updated to {status}")
        elif choice == "4":
            print("\nAll Current Orders: \n")
            for idx,order in enumerate(orders):
                print(f"{idx}:{order}")
            try:
                orders_index = int(input("\nWhat order are you updating? \n"))
                if 0 <= orders_index < len(orders):
                    order_selection = orders[orders_index]
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
            for idx,order in enumerate(orders):
                print(f"Order {idx}:{order}")
            try:
                orders_index = int(input("\nWhat order are you deleting? \n"))
                if 0 <= orders_index < len(orders):
                    deleted_order = orders.pop(orders_index)
                    print(f"\nOrder {deleted_order} deleted successfully")
                else:
                    print("\nInvalid choice, please choose again\n")
            except ValueError:
                print("\nInvalid number entered, try again :)\n")