def arithmetic(num1,num2):
    # perform 4 different mathermatical equations
    add = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quo = num1 / num2
    # return the four variables
    return add, diff, prod, quo 

print()
# ask for user input
num1 = int(input("Enter Number here! "))
num2 = int(input("Enter Number here! "))

# name the function based on the order in which it is returned
addition, subraction, multiplication, division = arithmetic(num1,num2)

# print the different variables in different prints 
# to show it is seperated
print()
print(f"The sum is {addition}")
print(f"The difference is {subraction}")
print(f"The product is {multiplication}")
print(f"The Quotient is {division}")
print()