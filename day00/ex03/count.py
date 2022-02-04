from string import punctuation

def text_analyzer(*args):

    text_analyzer.__doc__ = "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    # Variable
    p, u, l, s, t = 0, 0, 0, 0, 0
    if len(args) == 0:
        str = input("What is the text to analyse?\n")
    elif len(args) == 1:
        str = args[0]
    else:
        print('ERROR')
        return 
    for c in str:
        if c in punctuation:
            p += 1
        elif (c.isupper()):
            u += 1
        elif (c.islower()):
            l += 1
        elif (c.isspace()):
            s += 1
        t += 1
    total = f'The text contains {t} characters:'
    upper, lower = f'- {u} upper letters', f'- {l} lower letters'
    marks, space = f'- {p} punctuation marks', f'- {s} spaces'
    print(f'{total}\n{upper}\n{lower}\n{marks}\n{space}')


text_analyzer()
# text_analyzer()
print(text_analyzer.__doc__)
