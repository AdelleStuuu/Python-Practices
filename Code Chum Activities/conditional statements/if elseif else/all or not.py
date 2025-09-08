n1 = int(input('Enter first number: ')) 
n2 = int(input('Enter second number: ')) 
n3 = int(input('Enter third number: ')) 

if n1 > 0 and n2 > 0 and n3 > 0: 
    print('All numbers are positive.')
elif n1 < 0 and n2 < 0 and n3 < 0: 
    print('All numbers are negative.')
elif n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0: 
    print('All numbers are even.')
elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0: 
    print('All numbers are odd.')
else:
    print('Numbers are different.')