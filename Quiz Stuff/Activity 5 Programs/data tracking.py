print()
dataConsumed = int(input('Enter data consumed in GB: ')) 
maximumData = 100

avrgPerDay = round(dataConsumed /30,2) 
remaining = maximumData - dataConsumed
amountDue = dataConsumed * 10

if dataConsumed < maximumData:
    print('Average data per day:',avrgPerDay)
    print('Remaining data:',remaining)
    print('Amount Due in PHP:',amountDue)
else:
    print('Data consumed exceeds maximum data')

print()