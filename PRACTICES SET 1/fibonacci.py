print()
iter = int(input('input iterations for fibonacci sequence: '))
leftNumber = 0
rightNumber = 0
currentNumber = 0
i = 0
fibonacci = ''

while i != iter:
    if i == 0:
        fibonacci += '0,'
    elif i == 1:
        fibonacci += '1,'
        rightNumber = 1
    else: 
        currentNumber = leftNumber + rightNumber
        fibonacci += str(currentNumber)
        leftNumber = rightNumber
        rightNumber = currentNumber
        if i == iter - 1:
            fibonacci += '.'
        else:
            fibonacci += ','
    i += 1
    

print('the sequence is:',fibonacci) 
print()