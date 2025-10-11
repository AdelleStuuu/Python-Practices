def countdown(number):
    if number < 1:
        return 1
    else:
        print(number)
        countdown(number - 1)
print()
num = int(input("Enter a number: "))
print()
countdown(num)
print()