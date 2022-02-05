def kata00(t):
    print('The {ln} numbers are: {t}'.format(t=str(t)[1:-1], ln=len(t)))

t = (19, 42, 21, 0)
kata00(t)