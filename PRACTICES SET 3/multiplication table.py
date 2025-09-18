print()
while True:
    try:
        integer = int(input("Enter a number for their multiplication table: "))
    except ValueError:
        print("Not good, this is not an integer")
    else:
        break
print()
for i in range(11):
    if i == 0:
        continue
    else:
        value = i * integer 
        print(value)
print()