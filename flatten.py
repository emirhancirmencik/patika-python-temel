l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
m = []


def flatten_m(l):
    for i in range(len(l)):
        if isinstance(l[i], list):
            flatten_m(l[i])
        else:
            m.append(l[i])


flatten_m(l)
print(m)
