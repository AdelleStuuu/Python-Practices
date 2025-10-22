def arithmetic(num1,num2):
    add = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quo = num1 / num2

    return add, diff, prod, quo 
print()
num1 = int(input("Enter Number here! "))
num2 = int(input("Enter Number here! "))


addition, subraction, multiplication, division = arithmetic(num1,num2)
print()
print(f"The sum is {addition}")
print(f"The difference is {subraction}")
print(f"The product is {multiplication}")
print(f"The Quotient is {division}")
print()