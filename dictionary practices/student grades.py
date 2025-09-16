print()
print("Welcome to Adelle\'s grade lister !!!")
studentList = {
    'Katherina' : 95,
    'Orion' : 80,
    'Caeled' : 85,
    'Alter' : 75,
    'Sophie' : 90,
}
action = 0

while True:
    try:
        action = int("Input an action provided!\n1. Check grades\n2. Update Grades\n3. Add or Remove Students!")
    except ValueError:
        print("Input an integer.")
    else: 
        if action == 1 or action == 2 or action == 3:
            print("I see, good choice!")
            if action == 1:
                print("Okie dokie, here are the student List!")
                for student,grade in studentList.items():
                    if grade >= 90:
                        gradeLetter = 'A'
                    elif grade >= 80:
                        gradeLetter = 'B'
                    elif grade >= 70:
                        gradeLetter = 'C'
                    elif grade >= 60:
                        gradeLetter = 'D'
                    else:
                        gradeLetter = 'F'
                    print(f"Student Name {student}, Grade: {gradeLetter}")
        else: 
            print("Please pick a valid number!")