st = open('24_1302.txt').readline()
# while 'XZZY' in st:
#     st = st.replace('XZZY', 'XZZ ZZY')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')
count = 3

for i in range(len(st) - 3):
    if st[i : i + 4] != 'XZZY':
        count += 1
        maxx = max(maxx, count)
    else:
        count = 3
print(maxx)