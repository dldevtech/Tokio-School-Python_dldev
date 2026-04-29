def media(nums):
    if not nums:
        raise ValueError('lista vacía')
    return sum(nums) / len(nums)