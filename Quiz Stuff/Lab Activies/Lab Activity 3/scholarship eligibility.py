gpa = float(input('Enter GPA: '))
extracurricularActivites = int(input('Enter extracurricular activity hours: '))
volunteerHours = int(input('Enter volunteer hours: '))
points = 0

if gpa >= 5.00 or extracurricularActivites < 0 or volunteerHours < 0:
    print('An input is out of range.')
else:
    if gpa == 1.00 or gpa <= 1.50:
        points += 3
    elif gpa == 1.75 or gpa <= 2.25:
        points += 2
    elif gpa == 2.50 or gpa <= 3.00:
        points += 1
    
    if extracurricularActivites >= 100:
        points += 10
    else:
        points += 5

    if volunteerHours >= 100:
        points += 20
    else:
        points += 10
    
    print(f'Scholarship Eligibility Score is {points}.')