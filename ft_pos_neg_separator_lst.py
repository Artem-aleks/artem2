def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s


def ft_pos_neg_separator_lst(x):
    z = []
    c = []
    f = []
    n = []
    for i in x:
        if i == 0:
            c = c + [i]
        elif i > 0:
            f = f + [i]
        else:
            z = z + [i]
    n = [z, c, f]
    return n
