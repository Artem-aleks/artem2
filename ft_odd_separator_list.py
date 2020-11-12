def ft_len(b):
    s = 0
    for i in b:
        b += 1
    return b


def ft_odd_even_separator_lst(x):
    a = 0
    for i in x:
        a += 1
    r = a
    i = 0
    det = []
    srt = []
    num = []
    rum = [[0], [0]]
    for i in range(r):
        if x[i] > 0:
            det.append(x[i])
        elif x[i] < 0:
            srt.append(x[i])
        else:
            num.append(x[i])
        i += 1
    rum[0] = srt
    rum[1] = num
    rum[2] = det
    return rum