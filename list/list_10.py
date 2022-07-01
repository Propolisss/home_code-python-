list = [int(i) for i in input().split()]
maxx = list.index(max(list))
minn = list.index(min(list))

if len(list) != 0:
    list[maxx], list[minn] = list[minn], list[maxx]
print(' '.join(str(i) for i in list))