# Open and closing file examples

# # 1) without using with statement

file = open('cats.txt', 'w')
file.write('Raven') #This will overwrite whatever is already in the file. Basically starting over.
file.close()

# # 2) without using with statement

file = open('cats.txt', 'w')
try:    
    file.write('Rowen')    
    file.write('Raven')
finally:    
    file.close()

# py append-file.py will add data to the file WITHOUT overwriting it

# using with statement
with open('cats', 'w') as file:    
    file.write('Raven')