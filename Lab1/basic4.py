def merge_sort(nums):
    if len(nums) > 1:
        middle_num = len(nums) // 2
        left_side = nums[:middle_num]
        right_side = nums[middle_num:]
        merge_sort(left_side)
        merge_sort(right_side)
        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if int(left_side[i]) < int(right_side[j]):
                nums[k] = left_side[i]
                i += 1
            else:
                nums[k] = right_side[j]
                j += 1
            k += 1
        while i < len(left_side):
            nums[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            nums[k] = right_side[j]
            j += 1
            k += 1
