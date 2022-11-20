#import math
def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def palindrom(n):
    tmp = n
    b = 0
    while tmp != 0:
        b = b * 10 + tmp % 10
        tmp //= 10
    if n == b:
        return True
    return False
# def div_simple(n):
#     dels = set()
#     for i in range(2, int(n ** 0.5) + static):
#         if n % i == 0:
#             if simple(i):
#                 dels.add(i)
#             if simple(n // i):
#                 dels.add(n // i)
#     return dels
# def div_chet(n):
#     dels = set()
#     for i in range(2, int(n ** 0.5) + static):
#         if n % i == 0:
#             if i % 2 == 0:
#                 dels.add(i)
#             if (n // i) % 2 == 0:
#                 dels.add(n // i)
#     return dels
# def div(n):
#     dels = set()
#     for i in range(2, int(n ** 0.5) + static):
#         if n % i == 0:
#             dels |= {i, n // i}
#     return dels
nums = []
sums = []
count = 0

for i in range(1_000_000_000 + 1, 99, -1):
    summ = 1
    st = str(i)
    if st == st[::-1]:
        if simple(i):
            for i in range(len(st)):
                if st[i] != '0':
                    summ *= int(st[i])
            nums.append(i)
            sums.append(summ)
    count += 1
    if count == 1_000_000:
        print(i)
        count = 0

maxx = 0
maxx_n = 0
for i in range(len(sums)):
    if sums.count(sums[i]) > maxx:
        maxx = sums.count(sums[i])
        maxx_n = sums[i]

for i in range(len(nums)):
    if sums[i] == maxx_n:
        print(nums[i])

# maxx = 0
# maxx_index = 0
# for i in range(len(nums)):
#     if len(nums[i]) > maxx:
#         maxx = max(maxx, len(nums[i]))
#         maxx_index = i
#
# print(nums[maxx_index])