arr = []

isAppending = True 

while isAppending == True:
    num = int(input('Add an Array number: '))
    arr.append(num)
    willAppened = int(input('Will you Continue?\n1. yes\n2. no\nInput Answer: '))
    print()

    if willAppened == 1:
        isAppending = True
    else:
        isAppending = False

SortedArrAsc = sorted(arr)
SortedArrDesc = sorted(arr,reverse = True)

print("Original Array:",arr)
print("Ascending Array:",SortedArrAsc)
print("Descending Array:",SortedArrDesc)
print()