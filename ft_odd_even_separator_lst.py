def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s

def ft_odd_even_separator_lst(a):
    r = 0
    for i in a:
        r = r + 1
    t = r
    i = 0
    com = []
    num = []
    cn = [[0], [0]]
    for i in range(t):
        if a[i] % 2 == 0:
            com.append(a[i])
        elif a[i] % 2 != 0:
            num.append(a[i])
        i = i + 1
    cn[0] = num
    cn[1] = com
    return cn
