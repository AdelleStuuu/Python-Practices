vehicleClass = input('Enter vehicle class (1, 2, 3): ')
entryPoint = input('Enter entry point (A, B, C): ')
exitPoint = input('Enter exit point (X, Y, Z): ')
fee = 0


if vehicleClass == '1':
    fee += 100
    validityCheck = True
elif vehicleClass == '2':
    fee += 200
    validityCheck = True
elif vehicleClass == '3':
    fee += 300
    validityCheck = True
else:
    validityCheck = False

if validityCheck == True:
    if entryPoint == 'A':
        fee += 10
        validityCheck = True
    elif entryPoint == 'B':
        fee += 25
        validityCheck = True
    elif entryPoint == 'C':
        fee += 50
        validityCheck = True
    else:
        validityCheck = False

if validityCheck == True:
    if exitPoint == 'X':
        fee += 10
        validityCheck = True
    elif exitPoint == 'Y':
        fee += 25
        validityCheck = True
    elif exitPoint == 'Z':
        fee += 50
        validityCheck = True
    else:
        validityCheck = False

if validityCheck == True: 
    print(f'Toll Fee = {fee}')
else:
    print('Wrong Input')