print()
while True:
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print('Enter an integer value.')
        print()
        continue
    
    break

if not(year % 100 == 0):
    if year % 4 == 0: 
        print('It is a leap year!')
    else:
        print('oop, not a leap year...')
else:
    if year % 400 == 0:
        print('It is a leap year!')
    else:
        print('oop, not a leap year...')
print()