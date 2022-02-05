from sys import argv

usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"

if len(argv) == 3:
    if argv[1].isdecimal() and argv[2].isdecimal():
        a, b = int(argv[1]), int(argv[2])
        print('Sum: {:9d}'.format(a + b))
        print('Difference: {:2d}'.format(a - b))
        print('Product: {:5d}'.format(a * b))
        if b != 0:
            print('Quotient: {:10f}'.format(a / b))
            print('Remainder: {:2d}'.format(a % b))
        else:
            print('Quotient: {}'.format('ERROR (div by zero)'))
            print('Remainder: {}'.format('ERROR (modulo by zero)'))
    else:
        print("InputError: only numbers")
        print(usage)
elif len(argv) == 1:
    print(usage)
elif len(argv) > 3:
    print("InputError: too many arguments")
    print(usage)
else:
    print("InputError: too few arguments")
    print(usage)