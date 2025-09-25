add = 0
number = None
while number != 0:
    try:
        number = int(input("Input a number! "))
    except ValueError:
        print("Oop! that's no integer?")
    else:
        add += number 
print(add)