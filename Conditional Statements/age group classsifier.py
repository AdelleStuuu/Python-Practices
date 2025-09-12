print()
while True:
    try:
        age = int(input('Enter your age here: '))
    except ValueError:
        print('Enter a valid integer.')
        continue
    
    if 12 >= age >= 1: 
        print('you are a child!') 
        break
    elif 18 >= age >= 13:
        print('you are a teenager!')
        break
    elif 59 >= age >= 19: 
        print('you are an adult!')
        break
    elif 130 >= age >= 60: 
        print('you are a senior!')
        break
    else:
        print('please provide a valid age')
        print() 
print()   