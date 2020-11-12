def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_sum_even_lst(x):
    a = 0
    for i in x:
        a += 1
    i = 0
    t = a
    rem = 0
    for i in range(t):
        if x[i] % 2 == 0:
            rem = rem + x[i]
        i = i + 1
    return x
