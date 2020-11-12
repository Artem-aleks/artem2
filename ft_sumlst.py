def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s


def ft_sumlst(x):
    a = 0
    b = 0
    while b != ft_len(x):
        a += x[b]
        b += 1
    return a
