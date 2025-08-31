print()
burgers = int(input("Enter the number of burgers ordered: "))
fries = int(input("Enter the number of fries ordered: "))
sodas  = int(input("Enter the number of sodas ordered: "))

totalBurgers = burgers * 5
totalFries = fries * 3
totalSodas = sodas * 2

totalAmount = totalBurgers + totalFries + totalSodas

print()
print('The total amount is: ',totalAmount)
tendered = int(input('Enter amount tendered: '))
change = tendered - totalAmount
print('Your change is: ',change)
print()