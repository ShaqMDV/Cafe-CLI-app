# Taking information from week 3 (dictionaries) and implementing it into the app
import json

from products_menu import products_menu
from order_menu import orders_menu
from courier_menu import courier_menu

def load_products_read(products):
    with open('products.txt','r') as file:
        return json.load(file)
    return[]
def save_products_write(products, products_list):
    with open('products.txt','w') as file:
        json.dump(products_list, file, indent=3)

def load_couriers_read(couriers):
    with open('couriers.txt','r') as file:
        return json.load(file)
    return[]
def save_couriers_write(couriers, courier_list):
    with open('couriers.txt','w') as file:
        json.dump(courier_list, file, indent=3)

def load_orders_read(orders):
    with open('orders.txt', 'r') as file:
            return json.load(file)
    return []

def save_orders_write(orders, orders_list_dict):
    with open('orders.txt', 'w') as file:
        json.dump(orders_list_dict, file, indent=3)

products = load_products_read('products.txt')
couriers = load_couriers_read('couriers.txt')
orders = load_orders_read('orders.json')
order_status_options = ['Preparing', 'Out for delivery', 'Delivered']

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
            orders_menu()
        elif choice == "3":
            courier_menu()
        elif choice == "0":
            save_products_write('products.txt', products)
            save_couriers_write('couriers.txt', couriers)
            save_orders_write('orders.json', orders)
            print("\nData saved.\n")
            print("\nThanks for stopping by!\n")
            break
        else:
            print("Invalid choice, please try again :)\n")

main_menu()