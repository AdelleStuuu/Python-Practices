age = int(input('Enter your age: '))
income = int(input('Enter your income: $'))

if age > 60:
    if income < 10000: 
        print('Eligible for senior citizen discount')
    else:
        print('Not eligible for senior citizen discount')
else:
    print('Not eligible for senior citizen discount')