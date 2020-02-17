def quicksort_helper(nums, left, right):
    try:
        middle_num = int(nums[(left + right) // 2])
        i = left - 1
        j = right + 1
        while True:
            i += 1
            while int(nums[i]) < middle_num:
                i += 1
            j -= 1
            while int(nums[j]) > middle_num:
                j -= 1
            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]
    except ValueError as err:
        print(err)


def quicksort(nums, left=0, right=None):
    if right is None:
        right = len(nums) - 1

    def inner_sort(nums, left, right):
        if left < right:
            new_index = quicksort_helper(nums, left, right)
            inner_sort(nums, left, new_index)
            inner_sort(nums, new_index + 1, right)

    return inner_sort(nums, 0, len(nums) - 1)
