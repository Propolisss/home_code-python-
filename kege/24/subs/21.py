st = open('24_4627.txt').readline().strip()
# st = st.replace('NPO', '*').replace('PNO', '*').replace('P', ' ').replace('N', ' ').replace('O', ' ').split()
# print(max(len(i) for i in st))
maxx = float('-inf')

for j in 0, 1, 2:
    count = 0
    for i in range(j, len(st) - 2, 3):
        if st[i : i + 3] in ['NPO', 'PNO']:
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)