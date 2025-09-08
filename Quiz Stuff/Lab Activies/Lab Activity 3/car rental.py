age = float(input('Enter driver\'s age: '))
carDailyRate = float(input('Enter the car\'s daily rate: '))
rentalDays  = float(input('Enter rental days: '))
discount = .80
fee = 1000
price = carDailyRate * rentalDays

if age < 21: 
    print('Only drivers aged 21 years old or above can rent.')
else: 
    if age >= 60:
        price *= discount
    if rentalDays >= 30: 
        price += fee
    print(f'Your total cost is ${price:.2f}.')