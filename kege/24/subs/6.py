st = open('24_1040.txt').readline()
# for let in set(st) - set('0123456789'):
#     st = st.replace(let, ' ')
# print(max(len(i) for i in st.split()))
maxx = float('-inf')
count = 1
numbers = '0123456789'
for i in range(len(st) - 1):
    if st[i] in numbers and st[i + 1] in numbers:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)