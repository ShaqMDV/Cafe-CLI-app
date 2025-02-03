
from products_menu import products_menu
from order_menu import orders_menu
from courier_menu import courier_menu

def main_menu():
    print("\n Welcome to the Generation Cafe!\n") 
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
            orders_menu()
        elif choice == "3":
            courier_menu()
        elif choice == "0":
            print("\nData saved.\n")
            print("\nThanks for stopping by!\n")
            break
        else:
            print("Invalid choice, please try again :)\n")

main_menu()
 