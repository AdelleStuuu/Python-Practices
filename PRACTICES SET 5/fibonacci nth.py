def fibonacci(iteration): 
    # set all to zero initially
    value = pastNumber1 = pastNumber2 = 0
    # set a for loop that 
    for i in range(iteration):
        # zero is given
        if i == 0:
            pastNumber1 = 0
            value = 0 
        # one is also given
        elif i == 1:
            pastNumber2 = 1
            value = 1
        else: 
            # add two previous numbers
            value = pastNumber1 + pastNumber2
            # move the value of num2 to num1 
            # discard old value because computation is done
            pastNumber1 = pastNumber2
            # turn num2 to current value 
            # in order to store it in the next iteration
            # because value will be past value after this
            pastNumber2 = value
    # return the value
    return value

print()
# prompt user input
iteration =  int(input("Enter fibonacci iterations here! "))
# print the value 
print(f"The latest number based on the iteration is: {fibonacci(iteration)}")
print()