print()
print("Welcome to Adelle\'s grade lister !!!")
studentList = {
    'Katherina' : 95,
    'Orion' : 80,
    'Caeled' : 90,
    'Alter' : 75,
    'Sophie' : 80,
}
action = 0
def line():
    print("+--------------------------------+")

while True:
    print()
    line()
    print()
    try:

        action = int(input("Input an action provided!\n1. Check Database!!\n2. Update Grades~\n3. Add or Remove Students!\n4. Quit the Program\nEnter Answer: "))

    except ValueError:
        print("wOAH? Thats not an Integer?")

    else: 
        if action == 1 or action == 2 or action == 3 or action == 4:
            print()
            print("I see, good choice!")
            print()
            line()
            print()
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
                    print(f"Name: \"{student}\", Grade: {gradeLetter}")

            elif action == 2: 
                print("Updating Grades!")
                while True:
                    print()
                    studentName = input("Enter the Student's name! (its case sensitive!): ")
                    if studentName in studentList:
                        print(f"Okay! Found {studentName}! What to do now?")
                        while True:
                            try:
                                newGrade =  int(input("Enter Grade here: "))
                            except ValueError:
                                print("Silly billy, Grades are Integers!")
                            else:
                                studentList[studentName] = newGrade
                                break
                        print("Student Grade is updated!")
                        break
                    else:
                        print("Nope! Student is not here!")

            elif action == 3:
                while True:
                    print()
                    try:
                        addOrRemove = int(input("Well, Whatcha wanna do?\n1. Add a student\n2. Remove a student\nEnter Choice: "))
                    except ValueError:
                        print("Hmm, That doesn't seem like an integer?")
                    else:
                        print()
                        if addOrRemove == 1:
                            print("Great! A new Student!")
                            while True:
                                newStudentName = input("Enter their name here!: ")
                                studentNameSpliced = list(newStudentName)
                                for isLetter in studentNameSpliced:
                                    if isLetter.isdigit():
                                        isThereNumbers = True
                                        break
                                    else:
                                        isThereNumbers = False
                                if isThereNumbers == True:
                                    print("Hm, Why does the name have numbers?")
                                else:
                                    break
                            
                            while True:
                                try:
                                    newStudentGrade = int(input("Enter their grade here!: "))
                                except ValueError:
                                    print("Hi! That not an Integer!")
                                else:
                                    break
                            
                            studentList[newStudentName] = newStudentGrade
                            break

                        elif addOrRemove == 2:
                            print("Welp, Bye Bye Student!")
                            while True:
                                existingStudentname = input("Enter student name here!: ")
                                if existingStudentname in studentList:
                                    del studentList[existingStudentname]
                                    isDone = True
                                    break
                                else:
                                    print("That doesn't seem like a student in our records?")
                                    isDone = False
                            
                            if isDone == True:
                                break
                        
            elif action == 4: 
                print("See ya Later!")
                print()
                break

        else: 
            print("Please pick a valid number!")