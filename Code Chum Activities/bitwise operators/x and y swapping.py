n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
print(f'Before swap: num1 = {n1}, num2 = {n2}')

n1 = n1^n2
n2 = n1^n2
n1 = n1^n2

print(f'After swap: num1 = {n1}, num2 = {n2}')