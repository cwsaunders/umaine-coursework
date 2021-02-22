import math

# input
x = float(input())
y = float(input())
z = float(input())

# calculations
x1 = math.pow(x,z)
x2 = math.pow(x,math.pow(y,z))
x3 = math.fabs(x-y)
x4 = math.sqrt(math.pow(x,z))

# output
print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(x1, x2, x3, x4))