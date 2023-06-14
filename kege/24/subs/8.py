st = open('24_1975.txt').readline()
# while 'PP' in st:
#     st = st.replace('PP', 'P P')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')
count = 0

for i in range(len(st) - 1):
    if st[i] + st[i + 1] != 'PP':
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)