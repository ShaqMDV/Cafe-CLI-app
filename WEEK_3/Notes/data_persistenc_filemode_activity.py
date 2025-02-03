# writing to a file

def openwrite_file():
    with open('chickens.txt', 'w') as file:    
        print(" Adding data to file...")    
        file.write("Applemint\n") # Add First Chicken with open('data.txt', 'w') as variable: defines the variable, it doesn't have to be called file, and it's defined inside the with indent (which also automatically closes the file at the end)

def openwrite_plus_file():
    with open('chickens.txt', 'w+') as file:    
        print(" Adding data to file...")    
        file.write("Cartman\n")

def openread_file():
    with open('WEEK_3/Notes/products.txt', 'r') as file:    # Sometimes you have to be very specific with the path, so that python can find the file you are requesting.
        content = file.read()
        print(content)

def openread_plus_file():
    with open('chickens.txt', 'r+') as file:    
        content = file.read()   
        print(content)

def openappend_file():
    with open('chickens.txt','a') as file:
        print("Adding new names to the batch...")
        file.write("Jeremy\n") #Appending another name to this list

def openappend_plus_file():
    with open('chickens.txt','a+') as file:
        print("Adding new names to the batch...")
        file.write("Mark\n")

openread_file()