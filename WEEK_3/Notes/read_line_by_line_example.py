items = []
file = open("people.txt", 'r')
for line in file.readlines():    
    items.append(line.rstrip())
    print(items)
    file.close()
