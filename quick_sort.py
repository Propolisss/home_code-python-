def quick_sort(arr, left, right):
    if left >= right:
        return
    else:
        i = left
        j = right
        pivot = (left + right) // 2
        while i <= j:
            while arr[i] < arr[pivot]:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        quick_sort(arr, left, j)
        quick_sort(arr, i, right)
    return arr
nums = []


def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = len(arr) // 2
        left = []
        mid = []
        right = []
        for elem in arr:
            if elem < arr[pivot]:
                left.append(elem)
            elif elem > arr[pivot]:
                right.append(elem)
            else:
                mid.append(elem)
        return QuickSort(left) + mid + QuickSort(right)
    return arr


for i in range(10_000_000, 0, -1):
    nums.append(i)

#print(QuickSort(nums))
print(quick_sort(nums, 0, len(nums) - 1))
