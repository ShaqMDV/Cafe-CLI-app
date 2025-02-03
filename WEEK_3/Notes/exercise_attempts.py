people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

with open("names.txt","w") as file:
    for person in people:
        file.write(person + "\n")
        print("Names added still...")