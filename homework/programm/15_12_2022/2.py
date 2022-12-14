nums = [int(i) for i in open('17 (3).txt')]

def find_max_lett():
    global maxx, maxx_let
    dic = dict()
    for i in nums:
        n = abs(i)
        if len(str(n)) == 3:
            if str(n)[1] in dic:
                dic[str(n)[1]] += 1
            else:
                dic[str(n)[1]] = 1
    for i in dic:
        if dic[i] > maxx:
            maxx = dic[i]
            maxx_let = i

maxx = float('-inf')
maxx_let = ''
ans = []

find_max_lett()

for i in range(1, len(nums)):
    if (str(nums[i - 1])[-1] == maxx_let) or (str(nums[i])[-1] == maxx_let):
        ans.append(nums[i - 1] + nums[i])
print(len(ans), max(ans))