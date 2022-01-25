def quick_sort(arr, left, right):
    if left >= right:
        return

    constant_left = left
    pivot = arr[right]

    for i in range(constant_left, right):
        if arr[i] <= pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, constant_left, left - 1)
    quick_sort(arr, left + 1, right)


test_arr = [2, 3, 1, 5, 4, 9, 1, -1, 2, 3, 123, 123, 12, 3, 12, 2, 1, 2, 3, 2]
quick_sort(test_arr, 0, len(test_arr) - 1)
print(test_arr)
