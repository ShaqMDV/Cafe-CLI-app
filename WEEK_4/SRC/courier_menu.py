import csv

def load_couriers_read():
    with open('couriers.csv','r', newline='') as file:
        return list(csv.DictReader(file))
    return[]

def save_couriers_write(couriers):
    with open('couriers.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = couriers[0].keys())
        writer.writeheader()
        writer.writerows(couriers)
    print("Saved records to couriers list")

couriers = load_couriers_read()
 
def courier_menu():
    while True:
        print("\nCouriers Menu")
        print("1. View Couriers")
        print("2. Add Courier")
        print("3. Delete Courier")
        print("4. Update Courier")
        print("0. Back to Main Menu")
        choice = input("Choose an option: \n")

        if choice == "1":
            for idx, courier in enumerate(couriers, start=1):
                print(f"{idx}:{courier}")
                
        elif choice == "2":
            name = input("Enter Courier Name: ")
            price = float(input("What is the price of this service? "))
            phone_number = int(input("Enter the phone number for this service:"))
            couriers.append ({"name":name, "price":price,"phonenumber":phone_number})
            print("\nNew Courier added.\n")

        elif choice == "3":
            for idx, courier in enumerate(couriers, start=1):
                print(f"{idx}:{courier}")

            index = int(input("Which courier do you want to delete: ")) - 1

            del couriers[index]
            print(f"\n{index + 1}:{name} deleted")

        elif choice == "4":
            for idx, courier in enumerate(couriers, start=1):
                print(f"{idx}: {courier}")
            
                try:
                    idx = int(input("\nEnter the index of the courier you want to update: \n")) - 1
                    if 0 <= idx < len(couriers):  # Corrected the range check
                        new_name = input("\nWhat is the new name of the courier you would like to update? \n")
                        new_price = float(input("\nWhat is the new price of this service? \n"))
                        phone_number = input("\nWhat is the new phone number: \n")  # Keep as string for better phone number formatting
                        couriers[idx] = {"name": new_name, "price": new_price, "phonenumber": phone_number}
                        print("\nCourier updated! \n")
                        break  # Exit the loop after successful update
                    else:
                        print("\nInvalid index! Please enter a valid index within the range.\n")
                except ValueError:
                    print("\nInvalid input! Please enter a numeric value.\n")
                except IndexError:
                    print("\nIndex out of range! Please try again.\n")
                
        elif choice == "0":
            print("Saving changes...")
            save_couriers_write(couriers)
            break
        else:
            print("Invalid choice, please try again :)")