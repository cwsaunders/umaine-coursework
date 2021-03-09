fullname = input('')

namelist = fullname.split()

char1 = ''
char2 = ''

# Input: firstname, middlename, lastname
# Output: Lastname, Firstinitial, Middleinitial
if len(namelist) > 2:
    for i in range(len(namelist)):
        for j in range(len(namelist[i])):
            if i == 1:
                if j == 0:
                    char2 = namelist[i][j]
            if i == 0:
                if j == 0:
                    char1 = namelist[i][j]

if len(namelist) == 3:
    print(namelist[2] + ', ' + char1 + '.' + char2 + '.')


# Input: firstName lastName
# Output: lastName, firstInitial

if len(namelist) == 2:
    for i in range(len(namelist)):
        for j in range(len(namelist[i])):
            if i == 0:
                if j == 0:
                    char1 = namelist[i][j]


if len(namelist) == 2:
    print(namelist[1] + ', ' + char1 + '.')