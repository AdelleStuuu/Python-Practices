import math 
integer = int(input('Enter an integer: '))
squareRoot = math.sqrt(integer)
cubeRoot = math.cbrt(integer)
# Extra is needed because of CodeChum answer checker bug 
# where math.cbrt() doesn't work but math.pow() does
# and vice versa for math.pow()
cubeRoot2 = math.pow(integer, 1/3)

if cubeRoot.is_integer() or cubeRoot2.is_integer():
    if squareRoot.is_integer():
        print('Perfect in every way')
    elif cubeRoot % 2 == 0:
        print('Perfect in even cubes')
    else:
        print('Perfect in an odd way')
else:
    print('Nothing special')