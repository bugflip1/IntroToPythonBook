age = int(input('What is your current age? \n'))
hundred = 0

print(f'Your current age is {age}')


for future in range(10, 100, 10):
    if hundred == 1:
        break
    if age + future > 100:
        hundred = 1
        
    print(f'In {future} years, you will be '
          f' {age + future} years old.')
