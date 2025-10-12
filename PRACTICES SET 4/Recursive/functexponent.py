
def power(total,b,e,counter):
    if e == counter:
        print(f"the total power is {total}")
    else:
        total *= b 
        counter += 1
        power(total,b,e,counter)
        
    

print()
while True:
    try:
        base = int(input("Input the base: "))
    except:
        print("Enter an integer")
    else:
        break

while True:
    try:
        exponent = int(input("Input the exponent: "))
    except:
        print("Enter an integer")
    else:
        break


power(base,base,exponent,1)
print()

