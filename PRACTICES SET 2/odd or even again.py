print()
while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print('Enter an integer value.')
        print()
        continue
    
    break

if number % 2 == 0: 
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
print()