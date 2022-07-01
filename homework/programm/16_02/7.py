count = 0
sr = 0

def simple(n):
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(3000001, 10000000 + 1, 2):
    if simple(i):
        if simple(i + 2):
            count += 1
            sr = (i + i + 2) / 2
print(count)
print(sr)

# count = 0
# sr = 0
#
# def simple(n):
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# for i in range(500000, 1666666 + 1):
#     num = 6 * i - 1
#     numm = 6 * i + 1
#     if simple(num) and simple(numm):
#         можно убрать
#         if 3000000 < num < 10000000 and 3000000 < numm < 10000000:
#             count += 1
#             sr = (num + numm) / 2
# print(count)
# print(sr)