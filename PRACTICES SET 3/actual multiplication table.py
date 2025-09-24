iteration = 1
number = 1
print()
print("---------------------- Adelle's Multiplication Table! ----------------------")
print()
for i in range(10):
    number = 1
    for j in range(10):
        product = number * iteration
        print(product, end="\t")
        number += 1
    iteration += 1
    print()
print()
