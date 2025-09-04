kilometerPerHour = float(input('Enter kilometers per hour: '))
hoursTraveled = float(input('Enter number of hours traveled: '))
kilometer = kilometerPerHour * hoursTraveled
miles = kilometer * .621371
print(f'Distance in miles: {miles:.3f}')