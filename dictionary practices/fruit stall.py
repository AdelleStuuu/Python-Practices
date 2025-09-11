stall = {
    'Apples': 5,
    'Bananas': 2,
    'Oranges': 3,
    'Grapes': 4,
    'Mangoes': 6
}

print()
print("Welcome to Adelle's Fruit Stall!")
print(f"Apples : {stall['Apples']} in stock")
print(f"Bananas : {stall['Bananas']} in stock")
print(f"Oranges : {stall['Oranges']} in stock")
print(f"Grapes : {stall['Grapes']} in stock")
print(f"Mangoes : {stall['Mangoes']} in stock")
print()

while True:
    fruit = input('Enter the fruit you want to buy: ')

    if fruit in stall:
        break 
    else:
        print('Sorry, we do not have that fruit. Please choose from the available fruits:', ', '.join(stall.keys()))
        print()

while True:
    quantity = int(input('Enter the quantity you want to buy: '))

    if quantity <= stall[fruit]: 
        break
    else:
        print(f'Sorry, we only have {stall[fruit]} {fruit} in stock. Please enter a quantity less than or equal to {stall[fruit]}.')
        print()

print()
print(f'You have purchased {quantity} {fruit}!')
stall[fruit] -= quantity
print(f'Remaining {fruit} in stock: {stall[fruit]}')
print()
print("Thank you for shopping at Adelle's Fruit Stall!")
print()