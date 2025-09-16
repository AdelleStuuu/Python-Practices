while True:
    print()
    try:
        isItDivisible = int(input('Enter a number: '))
    except ValueError:
        print('Enter a valid integer.')
        continue
    else:
        if isItDivisible % 5 == 0 and isItDivisible % 3 == 0:
            print('It is divisible by both 5 and 3!')
            break
        elif isItDivisible % 3 == 0:
            print('It is only divisible by 3!')
            break
        elif isItDivisible % 5 == 0:
            print('It is only divisible by 5!')
            break
        else:
            print('That number is neither divisible by 5 or 3!')
print()