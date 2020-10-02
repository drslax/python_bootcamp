from random import shuffle


def generator(text, sep=" ", option=None):

    lst = text.split(sep)
    if option == 'shuffle':
        shuffle(lst)
    elif option == 'unique':
        lst = list(dict.fromkeys(lst))
    elif option == 'ordred':
        lst.sort()
    for i in lst:
        yield i


text = "Le Lorem,Ipsum,est,simplement,du,faux,texte,Le Lorem,Ipsum,est,simplement,du,faux,texte."
for word in generator(text, sep=",", option='ordred'):
    print(word)
