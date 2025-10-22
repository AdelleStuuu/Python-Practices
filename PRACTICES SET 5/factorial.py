def factorial(baseValue):
    # set both values to the base value given by user  
    value = lowerValue = baseValue
    # start an iteration with the base value minus 1 
    # to avoid the lower value reaching 0 
    for i in range(baseValue-1):
        # multiply value by its lower values
        value *= lowerValue-1
        # decrement lower value by 1
        lowerValue -= 1
    # return the final computation 
    return value
print()
# ask for user input
number = int(input("Enter a number for the factorial! "))
# print the final value 
# :, to separate numbers by comma ^^ 
# just to make it prettier!
print(f"The factorial of {number} is {factorial(number):,}")
print()