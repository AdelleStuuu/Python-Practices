personalInfo = {
    'name': 'Adelle Meitner',
    'age': 30,
}

print()
# pre update
print(personalInfo)

personalInfo.update(
    {
        'city': 'Las Vegas',
        'Occupation': 'Software Developer'
    }
)

# post update
print(personalInfo)
print()