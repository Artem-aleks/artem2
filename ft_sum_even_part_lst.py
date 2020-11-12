def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s


def ft_sum_even_part_lst(x):
    z = 0
    for i in x:
        if i % 2 == 0:
            z = z + i
    return z
