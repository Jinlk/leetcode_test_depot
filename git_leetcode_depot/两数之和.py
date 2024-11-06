nums = [3, 2, 4, 2]
target = 6

vv = []


# 两数之和
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                vv.append([i, j])
    return vv


print(twoSum(nums, target))
