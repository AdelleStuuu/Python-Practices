def counter(previousNumber,number):
    if previousNumber == -1:
        return 1
    else:
        print(number - previousNumber)
        counter(previousNumber - 1, number)
        

print()
num = int(input("Enter a number: "))
print()
counter(num-1,num)  
print()