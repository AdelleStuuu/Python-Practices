print()
factorialNumber = int(input("Enter your factorial number: "))
description = ''
print()
print(str(factorialNumber)+"! is equivalent to:")
numberList = factorialNumber

while numberList != 0:
    if numberList != 1:
        description += str(numberList)
        description += " * "
    else:
        description += str(numberList)
    numberList -= 1

print(description)

answer = 1  
while factorialNumber != 0:
    answer *= factorialNumber
    factorialNumber -= 1

print("the answer is:", answer)  
print()