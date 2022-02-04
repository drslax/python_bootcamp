import sys

string = ' '.join(sys.argv[1:])
ln = len(string)

if ln > 1:
    for c in string[::-1]:
        if c.isupper():
            print(c.lower(), end='')
        elif c.islower():
            print(c.upper(), end='')
        else:
            print(c, end='')
    print('')
