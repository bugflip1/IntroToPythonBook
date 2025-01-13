def between(num):
    if isinstance(num, float) and not num.is_integer():
        print(f'{num} is not a whole number! Sorry!')
        return
    elif isinstance(num, str):
        print(f'"{num}" is a string, not a number!')
        return
    if num < 0:
        print(f'{num} is less than 0!')
    elif num <= 50:
        print(f'{num} is between 0 and 50!')
    elif num <= 100:
        print(f'{num} is between 51 and 100!')
    elif num > 100:
        print(f'{num} is greater than 100')
    else:
        print('Some error occurred')

between(0)
between(50)
between(51)
between(100)
between(101)
between(75)
between(25)
between(30)
between(-12)
between(4.54)
between(856)
between(48.34)
between('this')