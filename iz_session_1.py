def task_1():
    a = []
    for i in range(0, 1001):
        if i % 3 == 0 and i % 5 == 0:
            a.append(i)
    return a


def task_2(a=""):
    l = 0
    n = 0
    for i in a:
        if i.isdigit():
            n = n + 1
        elif i.isalpha():
            l = l + 1
    return n, l


def task_3(a, b):
    for i in a:
        if i in b:
            a.remove(i)
            b.remove(i)
    for i in b:
        if i in a:
            a.remove(i)
            b.remove(i)

    return a, b


def task_4(a):
    b = ""
    for i in a:
        b = b + str(i)
    return int(b)


def task_5(a):
    return sorted(a)[0]


def task_6():
    pass
    ## Я не знаю как cделать


def task_7(a):
    b = []
    c = None
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
    for i in b:
        if a.count(i) == 1:
            c = i
            break

    return c
def task_8(a):
    d = []
    b = 1
    for i in range(0,len(a)):



        for j in a:
            if a[i] != j:
                b = b * j
                print(b)

        d.append(b)
        b = 1

    return(d)
