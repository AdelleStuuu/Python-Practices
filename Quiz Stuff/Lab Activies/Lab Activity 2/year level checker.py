level = int(input('Enter your year level: '))

if level == 1:
        levelYea = 'Freshman'
elif level ==  2:
        levelYea = 'Sophomore'
elif level ==  3:
        levelYea = 'Junior'
elif level ==  4:
        levelYea = 'Senior'
else:
        levelYea = 'Undefined'
        
if levelYea == 'Undefined':
    print(levelYea+".")
else:
    print(f'You are a {levelYea}.')