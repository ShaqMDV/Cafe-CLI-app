# Splitting data in a file
with open("message.txt", "r") as file:    
    data = file.readlines()    
    for line in data:        
        word = line.split()        
        print (word)