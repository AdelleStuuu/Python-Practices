dictionary1 = {
    'val 1 ' : 5,
    'val 6 ' : 6,
    'val 3 ' : 7,
    'val 4 ' : 5,
    'val 5 ' : 3,
    'val 2 ' : 2,
    'val 11' : 10
}

dictionary2 = {
    'val 9 ' : 5,
    'val 7 ' : 6,
    'val 3 ' : 7,
    'val 8 ' : 5,
    'val 10' : 3,
    'val 2 ' : 2,
}

dictionary3 = {}

for key,value in dictionary1.items():
    dictionary3.update({
        key : value, 
    })
for key,value in dictionary2.items():
    if key not in dictionary3:
        dictionary3.update({
            key: value,
        })

dictionary3 = sorted(dictionary3.items())
print()
print(f"old dictionary: {dictionary1}")
print(f"old dictionary: {dictionary2}")
print()
for key,value in dictionary3:
    print(f"key: {key}, value: {value}")
print()