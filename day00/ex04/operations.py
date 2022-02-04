from sys import argv

if len(argv) == 3:
    if argv[1].isdecimal() and argv[2].isdecimal():
        a, b = int(argv[1]), int(argv[2])
        print('Sum: {:10d}'.format(a + b))
        print('Sub: {:10d}'.format(a - b))
        print('Product: {:6d}'.format(a * b))
        if b != 0:
            print('Quotient: {:12f}'.format(a / b))
            print('Remainder: {:4d}'.format(a % b))
        else:
            print('Quotient: {}'.format('ERROR (div by zero)'))
            print('Remainder: {}'.format('ERROR (modulo by zero)'))
    else:
        print("InputError: only numbers")
else:
    print("InputError: too many arguments")
