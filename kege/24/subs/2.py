st = open('24_2420.txt').readline()
# st = st.replace('C', ' ').replace('D', ' ').split()
# print(max(len(i) for i in st))
maxx = float('-inf')
count = 1

for i in range(len(st) - 1):
    if st[i] in 'ABEF' and st[i + 1] in 'ABEF':
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)