st = open('24_1428.txt').readline()
# st = st.replace('XY', 'X Y').replace('XZ', 'X Z')
# print(max(len(i) for i in st.split()))
count = 1
maxx = float('-inf')

for i in range(len(st) - 1):
    if st[i] + st[i + 1] not in ['XY', 'XZ']:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)