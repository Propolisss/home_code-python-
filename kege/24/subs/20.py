st = open('24_4642.txt').readline().strip().replace('2', '1').replace('B', 'A')
# st = st.replace('A1', '*').replace('A', ' ').replace('1', ' ').split()
# print(max(len(i) for i in st))
maxx = float('-inf')

for j in 0, 1:
    count = 0
    for i in range(j, len(st) - 1, 2):
        if st[i : i + 2] == 'A1':
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)