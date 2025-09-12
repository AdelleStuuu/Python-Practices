print()
dictionary = { 
    'num1': 10,
    'num2': 20,
    'num3': 30
}

key = input('Enter the key you want to check: ')

print()
if key in dictionary:
    print(f'The key "{key}" exists in the dictionary with value: {dictionary[key]}.')
else:
    print(f'The key "{key}" does not exist in the dictionary.')
print()
