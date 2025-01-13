value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    pass # We dont care about 9
else:
    print('value is something else')

