# creating a csv
import csv
with open('people.csv', mode='w') as file:    
    fieldnames = ['first_name', 'last_name', 'age']    
    writer = csv.DictWriter(file, fieldnames=fieldnames)    
    writer.writeheader()    
    writer.writerow({'first_name': 'Jan',        
    'last_name': 'Smith',        'age': 60    })