print()
print("+--- Adelle's Market Property Value Assessment for Pipinos ---+")
print()
while True:
    try:
        taxAmount = float(input("Enter the amount you paid for taxes: "))
    except ValueError:
        print("Enter a float value")
    else:
        break

while True:
    try:
        yearsPaid = int(input("Enter the amount of years you paid for taxes: "))
    except ValueError:
        print("Enter an integer value")
    else:
        break

while True:
    try:
        inflationRate = float(input("Enter the inflation rate: "))
    except ValueError:
        print("Enter a float value")
    else:
        break

taxAndYearPaid = (taxAmount * yearsPaid)
fairMarketValue = f"{(taxAndYearPaid + (taxAndYearPaid +(taxAndYearPaid * (inflationRate/100)))) * yearsPaid:,}"

print()
print(f"The fair market value is {fairMarketValue} PHP")
print()