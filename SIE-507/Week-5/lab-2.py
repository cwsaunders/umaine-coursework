# Note: This is in Python 2.7

# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pet_name = input("Enter pet's name:\n")
random_number = input('Enter a number:\n')



print('You entered: ', end='')
print(favorite_color, pet_name, random_number)
print()


# Output two password options
password1 = favorite_color + '_' + pet_name
password2 = random_number + favorite_color + random_number
print('First password: ' + favorite_color + '_' + pet_name)
print('Second password: ' + random_number + favorite_color + random_number)
print()


# Output the length of the two password options
print('Number of characters in ' + str(password1) + ': ' + str(len(password1)))
print('Number of characters in ' + str(password2) + ': ' + str(len(password2)))