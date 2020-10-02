from time import sleep, time


def ft_progress(listy):

    lst = [i + 1 for i in listy]
    prc = 30
    p = ''
    mx = len(lst)
    start_time = time()

    for i in lst:
        elapsed_time = time() - start_time
        eta = ((mx - i) * elapsed_time) / i
        prc = int(i * 100 / mx)
        p = '=' * prc + '>'

        txt = 'ETA: {:.2f}s [{}%] [{:100s}] {}/{} | Eclapsed time {:.2f}s'.format(
            eta, prc, p, i, mx, elapsed_time)
        print(txt, end='\r')
        yield i


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
