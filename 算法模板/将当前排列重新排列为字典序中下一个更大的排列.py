def next_permutation(nums):
    """
    将当前排列重新排列为字典序中下一个更大的排列
    最大排列（例如[3,2,1]）的下一个排列是最小的排列（例如[1,2,3]）
    直接更新变量nums
    """

    # 寻找最靠右的顺序对：nums[i]<nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # 找到nums[i]右侧大于nums[i]的最小的数nums[j]，并交换nums[i]和nums[j]
    # 因为nums[i]右侧已倒序，所以从后向前找到的第1个就是最小的
    if i >= 0:
        j = len(nums) - 1
        while j >= i and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # 令nums[i]右侧的倒序数列变为顺序（交换后nums[i]右侧仍然保持倒序）
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
