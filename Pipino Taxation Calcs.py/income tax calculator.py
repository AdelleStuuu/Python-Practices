print()
print("+--- Adelle's Income Tax calculator for Pipinos ---+")
print()

while True:
    try:
        annualIncome = float(input("Enter your annual income! "))
    except ValueError:
        print("Enter a float value")
    else:
        break

print()
print("As per 2023's law...")
if annualIncome <= 250000:
    print("You are exempt from Income Taxation!")
elif annualIncome <= 800000:
    incomeTax = ((annualIncome - 400000) * .2) + 22500
elif annualIncome <= 2000000: 
    incomeTax = ((annualIncome - 800000) * .25) + 102500
elif annualIncome <= 8000000: 
    incomeTax = ((annualIncome - 2000000) * .3) + 402500
else:
    incomeTax = ((annualIncome - 8000000) * .3) + 2202500

if not(annualIncome <= 250000):
    print(f"Your Income Tax is {incomeTax:,} PHP") 

print()