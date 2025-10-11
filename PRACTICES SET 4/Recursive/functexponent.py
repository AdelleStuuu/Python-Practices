
def power(total,b,e,counter):
    if e == counter:
        print(f"the total power is {total}")
    else:
        total *= b 
        counter += 1
        power(total,b,e,counter)
        
    

print()
base = int(input("Input the base: "))
exponent = int(input("Input the exponent: "))

power(base,base,exponent,1)
print()

