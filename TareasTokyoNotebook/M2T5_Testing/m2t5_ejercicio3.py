def maximo_seguro(nums):
    if not nums:
        raise ValueError('lista vacía')
    maximo = nums[0]
    for n in nums[1:]:
        if n > maximo:
            maximo = n
    return maximo