# dictionary from csv
import csv
with open("chickens-data.csv", 'r') as file:
   chickens_dictionary = csv.DictReader(file)

   for chickens in chickens_dictionary:
          print(chickens)

# Some Dictionary Examples

list_of_keys = chickens.keys()
list_of_values = chickens.values()
single_item = chickens["Name"]
# all_items = chickens.items()

print(f'This is a list of Dictionary Keys', list_of_keys)
print(f'This is a list of Dictionary Values', list_of_values)
print(f'This is a single items value', single_item)
# print(f'Get all items', all_items)