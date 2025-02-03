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