file = open('27b.txt')
n = int(file.readline())

nums1 = [[] for i in range(5)]
nums2 = [[] for i in range(5)]
maxx_diff = float('-inf')

for i in range(n):
    n1, n2 = map(int, file.readline().split())
    if n1 >= n2:
        nums1[n1 % 5].append(n1)
        nums2[n2 % 5].append(n2)
    else:
        nums1[n2 % 5].append(n2)
        nums2[n1 % 5].append(n1)
    summ1 = 0
    summ2 = 0
    for j in range(len(nums1)):
        if sum(nums1[j]) > sum(nums2[j]):
            summ1 += sum(nums1[j])
            summ2 += sum(nums2[j])
        else:
            summ1 += sum(nums2[j])
            summ2 += sum(nums1[j])
    if abs(summ1 - summ2) % 5 == 0:
        maxx_diff = max(maxx_diff, abs(summ1 - summ2))
print(maxx_diff)