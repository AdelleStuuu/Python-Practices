score1 = int(input('Enter the first score: '))
score2 = int(input('Enter the second score: '))

if score1 > score2: 
    if score1 > 80: 
        print('Excellent!')
    else:
        print('Good job!')
else:
    print('Keep up the good work!')