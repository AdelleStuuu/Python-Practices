vehicleClass = input('Enter vehicle class (1, 2, 3): ')
entryPoint = input('Enter entry point (A, B, C): ')
exitPoint = input('Enter exit point (X, Y, Z): ')
fee = 0
validityCheck = True 

if vehicleClass == '1':
    fee += 100
elif vehicleClass == '2':
    fee += 200
elif vehicleClass == '3':
    fee += 300
else:
    validityCheck = False

if validityCheck == True:
    if entryPoint == 'A':
        fee += 10
    elif entryPoint == 'B':
        fee += 25
    elif entryPoint == 'C':
        fee += 50
    else:
        validityCheck = False

if validityCheck == True:
    if exitPoint == 'X':
        fee += 10
    elif exitPoint == 'Y':
        fee += 25
    elif exitPoint == 'Z':
        fee += 50
    else:
        validityCheck = False

if validityCheck == True: 
    print(f'Toll Fee = {fee}')
else:
    print('Wrong Input')