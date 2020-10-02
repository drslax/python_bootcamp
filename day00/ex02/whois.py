import sys

arg = sys.argv

if len(arg) == 2:
    if arg[1].isnumeric():
        if int(arg[1]) == 0:
            print('Zero')
        elif int(arg[1]) % 2 == 0:
            print('Even')
        else:
            print('Odd')
    else:
        print('ERROR')
else:
    print('ERROR')
