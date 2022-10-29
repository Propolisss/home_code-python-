def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    left = []
    mid = []
    right = []
    pivot = len(arr) // 2

    for i in arr:
        if i < arr[pivot]:
            left.append(i)
        elif i == arr[pivot]:
            mid.append(i)
        else:
            right.append(i)
    return quick_sort1(left) + mid + quick_sort1(right)

    return arr
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    left = []
    mid = []
    right = []
    pivot = len(arr) // 2

    for i in arr:
        if i > arr[pivot]:
            left.append(i)
        elif i == arr[pivot]:
            mid.append(i)
        else:
            right.append(i)
    return quick_sort2(left) + mid + quick_sort2(right)
def quick_sort_in_place_1(arr, left, right):
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
            quick_sort_in_place_1(arr, left, j)
            quick_sort_in_place_1(arr, i, right)
    return arr
def quick_sort_in_place_2(arr, left, right):
    if left >= right:
        return
    i = left
    j = right
    pivot = (i + j + 1) // 2
    while i <= j:
        while arr[i] > arr[pivot]:
            i += 1
        while arr[j] < arr[pivot]:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            quick_sort_in_place_2(arr, left, j)
            quick_sort_in_place_2(arr, i, right)
    return arr

nums = [int(i) for i in input().split()]

print(*(quick_sort_in_place_1(nums, 0, len(nums) - 1)))
print(*(quick_sort_in_place_2(nums, 0, len(nums) - 1)))