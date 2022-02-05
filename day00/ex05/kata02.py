def kata02(date):
    print('{0[3]:02d}/{0[4]:02d}/{0[2]:04d} {0[0]:02d}:{0[1]:02d}'.format(date))

t = (3,30,2019,9,2)

kata02(t)