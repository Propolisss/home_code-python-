def binary_search(array, item):
    first = 0
    last = len(array) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if array[midpoint] < item:
            first = midpoint + 1
        elif array[midpoint] > item:
            last = midpoint - 1
        else:
            return midpoint
    return -1

arr = [2, 5, 7, 8, 12, 14, 22, 54, 64, 232]
print(binary_search(arr, 64))