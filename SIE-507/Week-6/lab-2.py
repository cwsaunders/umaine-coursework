#setup for filling dictionary
contact_dict = {}
keys = []
values = []

# user input -- lineone is contacts -- linetwo is the pulled contact
lineone = input('').split()
linetwo = input('')

# assign keys and values from input
for i in range(len(lineone)):
    if i == 1:
        values.append(lineone[i])
    if i % 2 == 0:
        keys.append(lineone[i])
    if i % 2 != 0:
        if i != 1:
            values.append(lineone[i])


# fill dict with keys/values
for i in range(len(keys)):
    contact_dict.update({keys[i]:values[i]})
            


print(contact_dict.get(linetwo))

