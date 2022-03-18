def binary_search(arr, target):
    start = 0;
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

print(binary_search([1, 3, 5, 6], 5))
print(binary_search([-1, 0, 3, 5, 9, 12], 0))