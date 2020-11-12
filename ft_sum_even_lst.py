def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_sum_even_lst(lst):
    a = 0
    b = 0
    while b != ft_len(lst):
        a += lst[b]
        b += 2
    return a
