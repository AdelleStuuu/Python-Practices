num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = input("Choose operation (+, -, *, /): ")
if choice == '+':
    result = num1 + num2
elif choice == '-':
    result = num1 - num2
elif choice == '*':
    result = num1 * num2
elif choice == '/':
    result = num1 / num2
else:
    result = "Invalid operation"

print("The result is:", result)