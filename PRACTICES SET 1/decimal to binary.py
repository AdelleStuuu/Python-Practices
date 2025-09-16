number = int(input("Enter your Decimal Number: "))
nextNumber = number
uninvertedBinary = ''

while nextNumber > 1:
    isOneOrZero = int(nextNumber % 2)
    uninvertedBinary += str(isOneOrZero)
    number /= 2
    nextNumber = number
    
if nextNumber == 0 or nextNumber == 1:
    uninvertedBinary += nextNumber

invertedBinary = uninvertedBinary[::-1]
print('The binary equivalent is', invertedBinary)