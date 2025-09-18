personalInfo = {}
print()
name =  input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
occupation = input("Enter your occupation: ")

personalInfo['name'] = name
personalInfo['age'] = age   
personalInfo['city'] = city 
personalInfo['occupation'] = occupation

print()
print(f'name: {personalInfo['name']}')
print(f'age: {personalInfo['age']}')
print(f'city: {personalInfo['city']}')
print(f'job: {personalInfo['occupation']}')

print()