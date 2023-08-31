file = open('baumanka.txt')
points = dict()

for i in file:
    if 'сумма баллов' in i.lower():
        s = i.strip().split()
        temp = s[-4].split('-')[0]
        if any(j in s[-4] for j in ['11Б', '12Б', '13Б']) and 'ИУ6' in s[-4]:
            temp += '0'
        elif 'ИУ6' in s[-4]:
            temp += '1'
        if temp in points:
            points[temp].append( int(s[-1][:-1]) )
        else:
            points[temp] = [ int(s[-1][:-1]) ]

for i in sorted(points):
    #print(f'{i} проходной балл {min(points[i])} средний балл {round(sum(points[i]) / len(points[i]), 1)} максимальный балл {max(points[i])} зачислено {len(points[i])}')
    print(i, *sorted(points[i]))

count = 1
for i in sorted(points['ИУ5'] + points['ИУ60'] + points['РТ5'] + points['РК6'], reverse=True):
    print(i, count)
    count += 1