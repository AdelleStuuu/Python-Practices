integer1 = int(input('Enter first integer: '))
integer2 = int(input('Enter second integer: ')) 
integer3 = int(input('Enter third integer: ')) 
integer4 = int(input('Enter fourth integer: ')) 
integer5 = int(input('Enter fifth integer: ')) 
postiveCounter = 0
negativeCounter = 0
zeroCounter = 0

if integer1 > 0: 
    postiveCounter += 1
elif integer1 < 0:
    negativeCounter += 1 
elif integer1 == 0:
    zeroCounter += 1

if integer2 > 0: 
    postiveCounter += 1
elif integer2 < 0:
    negativeCounter += 1 
elif integer2 == 0:
    zeroCounter += 1

if integer3 > 0: 
    postiveCounter += 1
elif integer3 < 0:
    negativeCounter += 1 
elif integer3 == 0:
    zeroCounter += 1

if integer4 > 0: 
    postiveCounter += 1
elif integer4 < 0:
    negativeCounter += 1 
elif integer4 == 0:
    zeroCounter += 1

if integer5 > 0: 
    postiveCounter += 1
elif integer5 < 0:
    negativeCounter += 1 
elif integer5 == 0:
    zeroCounter += 1

print('Positive count:',postiveCounter)
print('Negative count:',negativeCounter)
print('Zero count:',zeroCounter)