
import csv

def load_orders_read():
    with open('orders.csv', 'r', newline='') as file:
           return list(csv.DictReader(file))
    return []

def load_couriers_read():
    with open('couriers.csv','r', newline='') as file:
        return list(csv.DictReader(file))
    return[]

def load_products_read():
        with open("products.txt", "r") as file:
            for line in file:
                name, price = line.strip().split(",")
                products_list.append({"name": name, "Price": float(price)})

products_list = []

def save_orders_write(orders):
    with open('orders.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)
    print("Saved records to orders")
    
products = load_products_read()

couriers = load_couriers_read()

orders = load_orders_read()

order_status_options = ['Preparing', 'Shipped', 'Delivered']

def orders_menu():
    while True:
        print("\n Orders Menu\n")
        print("1. View All Orders")
        print("2. Add New Order")
        print("3. Update Order Status")
        print("4. Update Order Details")
        print("5. Delete Order")
        print("0. Return to main menu")
        choice = input("Choose an option: \n") 

        if choice == "1":
            print("\n All current orders\n")
            for idx, order in enumerate(orders, start=1):
                print(f"{idx}: {order}")

        elif choice == "2":
            customer_name = (input("Enter New Customers Name Here: "))
            customer_address = (input("Enter New Customer Address Here: "))
            phone_number = (input("Enter New Customers Phone Number Here: "))
            
            print("Available Products: ")
            for idx, product in enumerate(products_list, start=1):
                print(f"{idx}:{product}")
            product_index = input("Enter the product indices you want to add to this order (comma-separated): ")
            selected_indices = ",".join(product_index.split(","))

            print("Available couriers:")
            for idx, courier in enumerate(couriers, start=1):
                print(f"{idx}: {courier}")
            courier_index = input("Enter the courier index: ")
            new_order = {
            "customer_name": customer_name,
            "customer_address": customer_address,
            "phone_number": phone_number,
            "products": selected_indices,
            "courier": courier_index,
            "status": "Preparing"
        }
            orders.append(new_order)
            print(f"\nNew order for {customer_name} created\n")

        elif choice == "3":
            print("\nAll Current Orders:\n")
            for idx,order in enumerate(orders, start=1):
                print(f"{idx}:{order}")

            order_index = int(input("\nWhat is the index of the order you would like to change?")) - 1

            print("\nOrder statues: ")
            for idx, status in enumerate(order_status_options, start=1):
                print(f"{idx}:{status}")

            status_index = int(input("\nEnter the index of the status you would like to update this order with: ")) - 1

            orders[order_index]['status'] = order_status_options[status_index]
            print(f"\nOrder status updated!")

        elif choice == "4":
            print("\nAll Current Orders: \n")
            for index, order in enumerate(orders, start=1):
                print(f"{index}: {order}")

            try:
                order_index = int(input("Enter order index to update: ")) - 1
                if order_index < 0 or order_index >= len(orders):
                    raise IndexError("Invalid index")
                selected_order = orders[order_index]

                for key, value in selected_order.items():
                    new_value = input(f"Enter new value for {key} (leave blank to keep '{value}'): ")
                    if new_value:
                        selected_order[key] = new_value
                        print(f"\nOrder updated successfully\n") # Loops through the keys and values, checking for new input to update into the dictionary.

            except(ValueError, IndexError):
                print("Invalid order index")
                return # Exit the function and lets the user try again.

        elif choice == "5":
            print("\nOrders list: \n")
            for idx,order in enumerate(orders, start=1):
                print(f"Order {idx}:{order}")
            try:
                orders_index = int(input("\nWhat order are you deleting? \n")) - 1
                if 0 <= orders_index < len(orders):
                    deleted_order = orders.pop(orders_index)
                    print(f"\nOrder {deleted_order} deleted successfully")
                else:
                    print("\nInvalid choice, please choose again\n")
                    return
            except ValueError:
                print("\nInvalid number entered, try again :)\n")

        elif choice == "0":
            print("Saving changes...")
            save_orders_write(orders)
            break
        else:
            print("Invalid input, please try again :)")
            