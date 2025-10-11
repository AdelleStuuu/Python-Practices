def whatIsLarger(x,y):
    if x >= y:
        return x
    elif y >= x:
        return y

print()
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

isItLarger = whatIsLarger(num1,num2)

print(f"the larger number between {num1} and {num2} is {isItLarger}\n")