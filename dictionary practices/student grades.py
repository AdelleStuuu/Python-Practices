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
        # variable asks the user for what action they'd choose based on the number
        action = int(input("Input an action provided!\n1. Check Database!!\n2. Update Grades~\n3. Add or Remove Students!\n4. Quit the Program\nEnter Answer: "))

    except ValueError:
        print("wOAH? Thats not an Integer?")

    else: 
        # condiitional checks what action the user chooses
        if action == 1 or action == 2 or action == 3 or action == 4:
            print()
            print("I see, good choice!")
            print()
            line()
            print()
            # block of code for checking the database
            if action == 1:
                print("Okie dokie, here are the student List!")
                # conditional that converts the grades from integer to Letters
                for student,grade in studentList.items():
                    if grade >= 90:
                        # checks whether the student is qualified of being with honors
                        if grade >= 95:
                            gradeLetter = 'A+'
                        else:
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
            # conditional that updates a current student's grades
            elif action == 2: 
                print("Updating Grades!")
                while True:
                    print()
                    studentName = input("Enter the Student's name! (its case sensitive!): ")
                    #checks whether the student is in the database
                    if studentName in studentList:
                        print(f"Okay! Found {studentName}! What to do now?")
                        while True:
                            # block that updates the integer grade
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
                # asks if you either want to add or remove a student
                while True:
                    print()
                    # asks the user for their input 
                    try:
                        addOrRemove = int(input("Well, Whatcha wanna do?\n1. Add a student\n2. Remove a student\nEnter Choice: "))
                    except ValueError:
                        print("Hmm, That doesn't seem like an integer?")
                    else:
                        print()
                        # block of code that adds a new students
                        if addOrRemove == 1:
                            print("Great! A new Student!")
                            # makes sure if the name does not contain a number
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
                            # makes sure that the grade entered is an integer value
                            while True:
                                try:
                                    newStudentGrade = int(input("Enter their grade here!: "))
                                except ValueError:
                                    print("Hi! That not an Integer!")
                                else:
                                    break
                            
                            studentList[newStudentName] = newStudentGrade
                            break
                        # block of code that adds a new students
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
            # exit out of the program
            elif action == 4: 
                print("See ya Later!")
                print()
                exit()

        else: 
            print("Please pick a valid number!")