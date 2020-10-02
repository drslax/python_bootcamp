# --------------- kata00 ---------------
def kata00(t):
    print('The 3 numbers are:', str(t)[1:-1])


#t = 19, 42, 21
# kata00(t)

# --------------- kata01 ---------------

def kata01(dics):
    for k, v in dics.items():
        print(k, 'was created by', v)


# languages = {
#     'Python': 'Guido van Rossum',
#     'Ruby': 'Yukihiro Matsumoto',
#     'PHP': 'Rasmus Lerdorf',
# }
# kata01(languages)

# --------------- Kata02 ---------------


def kata02(date):
    print('{0[3]}/{0[4]}/{0[2]} {0[0]}:{0[1]}'.format(date))


# date = (3, 30, 2019, 9, 25)
# kata02(date)


def kata03(phrase):
    print('{:->42s}'.format(phrase))


# kata03('Test')
