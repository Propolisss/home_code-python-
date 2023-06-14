st = open('24_4602.txt').readline().strip().replace('C', 'B').replace('D', 'B').replace('O', 'A')
# st = st.replace('BA', '*').replace('B', ' ').replace('A', ' ')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')

for j in 0, 1:
    count = 0
    for i in range(j, len(st) - 1, 2):
        if st[i] + st[i + 1] == 'BA':
            count += 1
            maxx = max(maxx, count)
        else:
            count = 0
print(maxx)