l = [[1, 2], [3, 4], [5, 6, 7]]


def l_reverse(l):
    for i in range(len(l)):
        if isinstance(l[i], list):
            l_reverse(l[i])
    l.reverse()


l_reverse(l)
print(l)

