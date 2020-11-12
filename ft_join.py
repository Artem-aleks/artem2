def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s


def ft_join(x, s=" "):
    z = ""
    for i in range(ft_len(x) - 1):
        z = z + str(x[i])
        z = z + s
    z = z + str(x[-1])
    return z
