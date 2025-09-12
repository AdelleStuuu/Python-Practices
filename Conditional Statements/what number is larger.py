print()
number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
print()
if number1 > number2: 
    print(f'{number1} is greater than {number2}.')
elif number1 < number2: 
    print(f'{number2} is greater than {number1}.')
else:
    print(f'Both {number1} and {number2} are equal.')
print()