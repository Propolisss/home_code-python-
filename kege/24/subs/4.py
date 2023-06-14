st = open('24_865.txt').readline()
# st = st.replace('C', ' ').replace('F', ' ').split()
# print(max(len(i) for i in st))
maxx = float('-inf')
count = 1
for i in range(len(st) - 1):
    if st[i] not in 'CF' and st[i + 1] not in 'CF':
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)