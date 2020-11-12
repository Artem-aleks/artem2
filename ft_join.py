def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_join(s, g):
    a = ""
    b = 0
    if not g:
        g = " "
    while b != ft_len(s) - 1:
        a += s[b] + g
    a = a + s[-1]
    return a
