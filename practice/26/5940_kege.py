from functools import lru_cache
file = open('practice/26.txt')

@lru_cache(None)
def find_road(n):
    if (n + 1) in dic and (n + 2) in dic:
        return max(find_road(n + 1), find_road(n + 2))
    elif (n + 1) in dic:
        return find_road(n + 1)
    elif (n + 2) in dic:
        return find_road(n + 2)
    else:
        return n
@lru_cache(None)
def find_summ(n, summ):
    if (n + 1) in dic and (n + 2) in dic:
        if dic[n][0] < dic[n][1]:
            return find_summ(n + 1, summ + dic[n][0])
        else:
            return find_summ(n + 2, summ + dic[n][1])
    elif (n + 1) in dic:
        return find_summ(n + 1, summ + dic[n][0])
    elif (n + 2) in dic:
        return find_summ(n + 2, summ + dic[n][0])
    else:
        return summ

n = int(file.readline())
nums = []
dic = {}
minn_id = float('inf')

for i in range(n):
    temp_arr = [int(i) for i in file.readline().split()]
    nums.append(temp_arr)
    dic[temp_arr[0]] = []
    minn_id = min(minn_id, temp_arr[0])

for i in range(n):
    for j in range(1, len(nums[i])):
        if (nums[i][0] + j) in dic:
            dic[nums[i][0]].append(nums[i][j])

maxx_id = find_road(minn_id)
minn_summ = find_summ(minn_id, 0)
print(minn_summ, maxx_id)