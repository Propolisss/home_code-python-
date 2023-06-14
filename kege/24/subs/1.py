st = open('24_2419.txt').readline()
# for i in set(st) - {'C'}: st = st.replace(i, ' ')
# print(st.split())
# print(max(len(i) for i in st.split()))
maxx = float('-inf')
count = 1
for i in range(len(st) - 1):
    if st[i] == st[i + 1]:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)