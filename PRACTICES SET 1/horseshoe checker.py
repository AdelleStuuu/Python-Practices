horseshoes = []
iter = 0
print()
while iter < 4:
    horseshoe = int(input("Add a horse shoe: "))
    horseshoes.append(horseshoe)
    iter += 1

uniques = 4 - len(set(horseshoes))
print()

if uniques == 1:
    print(f"You need to buy {uniques} unique horse shoe!")
else:
    print(f"You need to buy {uniques} unique horse shoes!")
print()