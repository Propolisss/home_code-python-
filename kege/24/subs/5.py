st = open('24_2426.txt').readline()
# st = st.replace('B', ' ').replace('A', ' ').replace('C', ' ')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')
count = 1
for i in range(len(st) - 1):
    if st[i] in '123' and st[i + 1] in '123':
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)