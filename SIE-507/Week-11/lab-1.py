num_of_integers = int(input(''))

items = []
smallest = 0
for i in range(num_of_integers):
    items.append(int(input('')))

for i in range(len(items)):
    if i == 0:
        smallest = items[i]
    if items[i] < smallest:
        smallest = items[i]

for i in range(len(items)):
    items[i] -= smallest

for i in range(len(items)):
    print(items[i])
