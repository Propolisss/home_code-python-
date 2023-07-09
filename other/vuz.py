file = open('baumanka.txt')
points = dict()

for i in file:
    if 'сумма баллов' in i.lower():
        s = i.strip().split()
        temp = s[-4].split('-')[0]
        if temp in points:
            points[temp].append( int(s[-1][:-1]) )
        else:
            points[temp] = [ int(s[-1][:-1]) ]

for i in sorted(points):
    print(f'{i} проходной балл {min(points[i])} средний балл {round(sum(points[i]) / len(points[i]), 1)} максимальный балл {max(points[i])}')