def collatz(number):
    if number == 1:
        print '1'
        return 1
    elif number % 2 == 0:
        print number/2
        return number/2
    else:
        print 3*number+1
        return 3*number+1
        
def execute():
    while True:
        number = input('What is your number?: ')
        try:
            int(number)
        except:
            print('Please provide an integer.')
            continue
        break
        
    while number is not 1:
        number = collatz(number)
