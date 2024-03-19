from math import sqrt
number = int(input('Enter a number: '))
try:
    x = sqrt(number)
    print(f'The square root of {number} is {x}')
except ValueError:
    print('Number must be a positive.')