print()
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

num = int(input("Enter num: "))

print(f"The fact is that this is {factorial(num):,}")
print()