fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
# If the iteration returns that fruit is banana, then this
# checks "is the current item equal to banana?"
# so since it is, it will NOT carry on with the iteration.

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
# This tells the terminal to end the current iteration at "Banana"
# It then continues after the that condition has been identified
# In essesence it is telling the terminal to "skip" a certain value


# Example
# chickens = ["Arnie", "Janet", "Shiv"]
# for chicken in chickens:    
#     if chicken == "Shiv":        
#         print("My favourite chicken is Shiv")        
#         print("We are going to continue and not run any other code in the for loop")        
#         continue    
#     print("The other chickens are not my favourites")
#     print("I feed the chickens every day") 

#For Else statement
for x in range(6):
    if i == "required":
        break
else:
    raise ValueError("Required not found.")
print("Required was found")
