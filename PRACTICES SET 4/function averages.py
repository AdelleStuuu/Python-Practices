def average(list):
    sum = counter = 0
    for number in list:
        sum += number
        counter += 1
    
    ave = sum / counter
    print(f"The average is {ave:.2f}")

list1 = [1,2,3,43,2,25,3242,425,32]
list2 = [1,2,5,42,3,6,7,23,454,46,45]
list3 = [1,5,2,6,7,8,43,65,77,12,14,54]
list4 = [1,6,5,4,76,45,23,13,65,765,45]

print()
average(list1)
average(list2)
average(list3)
average(list4)
print()
