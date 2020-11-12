def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_rmstrspc(x):
    a = ""
    b = 0
    while b != ft_len(x):
        if x[b] != " ":
        a = a + x[b]
        b = b + 1
    return a
