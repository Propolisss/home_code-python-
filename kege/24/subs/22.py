st = open('24_4643.txt').readline().strip().replace('B', 'A').replace('2', '1')
# st = st.replace('11A', '*').replace('1', ' ').replace('A', ' ')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')

for j in 0, 1, 2:
    count = 0
    for i in range(j, len(st) - 2, 3):
        if st[i : i + 3] == '11A':
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)