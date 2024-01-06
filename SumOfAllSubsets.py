def subsetXORSum(nums):
    xorSum = 0
    subsetCount = 2 ** len(nums)
    for i in range(subsetCount):
        subsetXOR = 0
        for j in range(len(nums)):
            if (i & (1 << j)) > 0:
                subsetXOR ^= nums[j]
        xorSum += subsetXOR
    return xorSum
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(subsetXORSum(nums))
