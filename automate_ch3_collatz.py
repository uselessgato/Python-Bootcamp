def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(number*3+1)
        return number*3+1

while True:
    num = input('Enter an integer and see magic happen: \n')
    try:
        num = int(num)
    except:
        print()
        print('Only integers are accepted\n')
        continue
    break

while num != 1:
    num = collatz(num)
