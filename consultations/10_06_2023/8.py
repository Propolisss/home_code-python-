from itertools import *
ch = '0246'
nech = '135'
count = 0

for i in product('0123456', repeat=6):
    st = ''.join(i)
    if st[0] != '0' and st[-1] not in '0123' and sum(1 for j in st if j in ch) == sum(1 for j in st if j in nech):
        count += 1
print(count)

# def to_base(n, base):
#     temp_n = n
#     arr = []
#
#     while temp_n:
#         arr = [temp_n % base] + arr
#         temp_n //= base
#     return arr
#
# count = 0
#
# for i in range(1, 10_000_000):
#     n = to_base(i, 7)
#     if len(n) == 6:
#         if n[-1] not in [0, 1, 2, 3] and (sum(1 for j in n if j in [0, 2, 4, 6]) == sum(1 for j in n if j in [1, 3, 5])):
#             count += 1
# print(count)