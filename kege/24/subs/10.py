st = open('24_21.txt').readline()
# while 'XX' in st:
#     st = st.replace('XX', 'X X')
# while 'YY' in st:
#     st = st.replace('YY', 'Y Y')
# while 'ZZ' in st:
#     st = st.replace('ZZ', 'Z Z')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')
count = 1
for i in range(len(st) - 1):
    if st[i] != st[i + 1]:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)