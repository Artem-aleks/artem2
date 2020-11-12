def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s


def ft_odd_even_separator_lst(x):
    z = []
    c = []
    f = []
    for i in x:
        if i % 2 == 0:
            z = z + [i]
        elif i % 2 != 0:
            c = c + [i]
    f = [z, c]
    return f
