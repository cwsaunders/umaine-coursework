lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingrdients
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print('')
print('Lemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave))
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
print('')
n_servings = float(input('How many servings would you like to make?\n'))
print('')
agave_conv = agave/servings
water_conv = water/servings
lemon_juice_conv = lemon_juice/servings

agave_final = agave_conv*n_servings
water_final = water_conv*n_servings
lemon_juice_final = lemon_juice_conv*n_servings

print('Lemonade ingredients - yields {:.2f} servings'.format(n_servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice_final))
print('{:.2f} cup(s) water'.format(water_final))
print('{:.2f} cup(s) agave nectar'.format(agave_final))
# FIXME (3): Convert and output the ingredients from (2) to gallons
print('')
water_gallon = water_final/16
agave_gallon = agave_final/16
lemon_juice_gallon = lemon_juice_final/16

print('Lemonade ingredients - yields {:.2f} servings'.format(n_servings))
print('{:.2f} gallon(s) lemon juice'.format(lemon_juice_gallon))
print('{:.2f} gallon(s) water'.format(water_gallon))
print('{:.2f} gallon(s) agave nectar'.format(agave_gallon))