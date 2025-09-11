print()
quiz =  float(input('Enter score in Quiz: '))
classStanding =  float(input('Enter score in Class Standing: '))
nonAcademics =  float(input('Enter score in Non-Academics: '))
major =  float(input('Enter score in Major Exam: '))

compQuiz = quiz * .35 
compStanding = classStanding * .2
compAcads = nonAcademics * .05
compExam = major * .4

totalGrade = compQuiz + compStanding + compAcads + compExam

print()
print(f'Your Grade is: {totalGrade:.2f}')
print()