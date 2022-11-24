def numberquiz(num,att):
    yield "Назовите число:"
    for i in att:
        if i > num:
            yield "это больше",i
        elif i < num:
            yield"это меншьше",i
        else:
            yield"да это",i
a = numberquiz(5,[3,7,5])
for i in a:
    print(*i)
