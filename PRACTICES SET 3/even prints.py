number = None
numberList = []
print()
while number != 0:
    number = int(input("Enter yer Number! "))
    if number != 0:
        numberList.append(number) 

print()
for i in numberList:
    if i % 2 == 0 and i != 0:
        print(f"This number is even in the list {i}")

print()