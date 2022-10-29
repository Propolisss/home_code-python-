def quick_sort(arr, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = (i + j + 1) // 2
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
nums = [4, 5, 1, 2, 3, 8]


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




#print(QuickSort(nums))
print(quick_sort(nums, 0, len(nums) - 1))
