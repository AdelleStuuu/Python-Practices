def evenNumbers(number):
    if 0 == number :
        return 1
    else:
        print(number + number - 2)
        evenNumbers(number - 1)

num = int(input("Enter a number: "))
print()
evenNumbers(num)
print()