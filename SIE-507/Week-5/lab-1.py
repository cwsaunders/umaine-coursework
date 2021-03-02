# Note -- in Python 2.7

current_price = int(input())
last_months_price = int(input())
mortgage = (current_price * 0.051) / 12

print('This house is $', end='')
print(current_price, end='')
print('. The change is $', end='')
print(current_price-last_months_price, end='')
print(' since last month.')
print('The estimated monthly mortgage is $', end='')
print('{:.2f}'.format(mortgage), end='.\n')

