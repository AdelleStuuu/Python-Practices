number = 2
i = 0 
print()
iterations = int(input('enter amount of iterations: '))

print()
while i < iterations:
    if number % 2 == 0:
        print(number)
        number += 1
        i += 1
    else:
        number += 1
print()