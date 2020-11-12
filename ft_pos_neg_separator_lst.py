def ft_len(b):
    s = 0
    for i in b:
        s += 1
    return s

def ft_odd_even_separator_lst(x):
    a = 0
    for i in x:
        a += 1
    vt = a
    i = 0
    t = []
    nc = []
    num = []
    com = [[0], [0]]
    for i in range(vt):
        if x[i] > 0:
            t.append(x[i])
        elif x[i] < 0:
            nc.append(x[i])
        else:
            num.append(x[i])
        i += 1
    com[0] = nc
    com[1] = num
    com[2] = c
    return com
