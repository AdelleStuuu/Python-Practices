def oddNumbers(number):
    if 0 == number :
        return 1
    else:
        print(number + number - 1)
        oddNumbers(number - 1)

num = int(input("Enter a number: "))
print()
oddNumbers(num)
print()