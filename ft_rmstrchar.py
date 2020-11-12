def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s


def ft_rmstrchar(x, n):
    z = ""
    num = 0
    for i in x:
        if i not in n:
            z = z + i
        if i in n:
            num = num + 1
    return z
