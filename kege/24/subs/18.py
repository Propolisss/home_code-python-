st = open('24_66.txt').readline().strip()
# st = st.replace('KOT', '*').replace('K', ' ').replace('O', ' ').replace('T', ' ').split()
# print(max(len(i) for i in st))
maxx = float('-inf')

for j in 0, 1, 2:
    count = 0
    for i in range(j, len(st) - 2, 3):
        if st[i : i + 3] == 'KOT':
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)