def power(base, exponent):
    # define it by 1 so the base can multiply to it 
    result = 1 
    # a for loop to iterate depending on how 
    # much the exponent is
    for i in range(exponent):
        # multiply the base every iteration
        result *= base
    # return the result
    return result

print()
# without user input
print(power(12,4))
print(power(10,10))
print()
# with user input
base = int(input("Enter the base here: "))
exponent = int(input("Enter the exponent here: "))
print(power(base,exponent))
print()