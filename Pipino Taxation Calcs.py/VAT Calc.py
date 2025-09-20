print()
print("+--- Adelle's VAT calculator for Pipinos ---+")
print()

while True:
    try:
        taxableSales = float(input("Enter amount of taxable sales: "))
    except ValueError:
        print("Enter a float value")
    else:
        break
print()
ValueAddedTax = taxableSales * .12
print(f"Your VAT tax is about {ValueAddedTax} PHP")
print()