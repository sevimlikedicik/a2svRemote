def merge_subarrays(arr, left, mid, right):
    new_arr = []
    constant_mid = mid
    constant_left = left
    while left < constant_mid or mid <= right:
        if left >= constant_mid:
            new_arr.append(arr[mid])
            mid += 1
        elif mid > right:
            new_arr.append(arr[left])
            left += 1
        else:
            if arr[left] < arr[mid]:
                new_arr.append(arr[left])
                left += 1
            else:
                new_arr.append(arr[mid])
                mid += 1

    for i, num in enumerate(new_arr):
        arr[constant_left + i] = num

    return


def merge_sort(arr, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge_subarrays(arr, left, mid + 1, right)
    return


test_arr = [2, 3, 1, 5, 4, 9, 1, -1, 2, 3]
merge_sort(test_arr, 0, len(test_arr) - 1)
print(test_arr)
