st = open('24_2421.txt').readline()
# st = st.replace('D', ' ').split()
# print(max(len(i) for i in st))
maxx = float('-inf')
count = 1
for i in range(len(st) - 1):
    if st[i] != 'D' and st[i + 1] != 'D':
        count += 1
        maxx = max(count, maxx)
    else:
        count = 1
print(maxx)