import random 
randomNum = random.randint(1,100)
print()
print('+--- Welcome to Adelle\'s number game!!! ---+')

while True:
    print()
    try: 
        difficulty = int(input('Enter a difficulty setting: \n1. Easy\n2. Medium\n3. Hard\n4. Precise\nEnter here: '))
    except ValueError:
        print('Enter an integer value.')
    else:
        if difficulty == 1:
            randNumRange = randomNum - 15
            break
        elif difficulty == 2:
            randNumRange = randomNum - 10
            break
        elif difficulty == 3:
            randNumRange = randomNum - 5
            break
        elif difficulty == 4:
            randNumRange = randomNum
            break
        else:
            print('Oop, I sense an invalid difficulty!') 

while True:
    print()
    try:
        number = int(input('Enter a number [1-100]: '))
    except ValueError:
        print('Enter an Integer.')
        continue
    else:
        if number <= 0:
            print('Oop, Cant choose something equal to or less than 0!')
        elif randomNum >= number >= randNumRange:
            print('The number is within range! Good job!')
            break
        elif randomNum < number < randNumRange:
            print('Oop, Try higher!')
        else:
            print('Oop, Try lower!')
print()

