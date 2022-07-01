file = open('file.txt')
n = int(file.readline())
nums = []


def factorize(number):
    dels = list()
    i = 2
    while number != 1:
        if number % i == 0:
            number //= i
            dels.append(i)
            continue
        else:
            i += 1
    return dels


for i in range(n):
    nums.append((int(file.readline())))
# print(nums)

# alldels = set()
#
# for i in range(n):
#     alldels.update(nums[i])
# # print(alldels)
#
# maximum = len(alldels)

number = 345600
tmp_arr = [0] * n
count = 0
for i in range(n):
    tmp_arr = [0] * n
    tmp_arr[i] = nums[i]
    for k in range(i + 1, n):
        tmp_arr[k] = tmp_arr[k - 1]*(nums[k])
        if (tmp_arr[k]%345600)==0:
            count+=k-i
            break
        if k==n-1:
            count+=k-i+1

print(count)
