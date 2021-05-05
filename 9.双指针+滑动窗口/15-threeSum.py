"""
三数之和：
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

 满足要求的三元组集合为：
 [[-1, 0, 1], [-1, -1, 2]]
"""
from typing import List


# 这样会超时
class Solution:
    def twoSum(self, nums, target):
        "给定 nums = [2, 7, 11, 15], target = 9， return [0, 1]"
        d = {}
        result = []
        for i in range(len(nums)):
            # if nums[i]==cur:
            #     continue
            # print(nums[i],target-nums[i], d,target-nums[i] in d)
            if target - nums[i] in d:
                result.append([nums[i], nums[d[target - nums[i]]]])
            d[nums[i]] = i

        return result

    def drop_duplicates(self, res):
        res_set = [set(i) for i in res]
        new_res_idx = []
        new_res = []
        for i, each in enumerate(res_set):
            if each not in new_res_idx:
                new_res_idx.append(each)
                new_res.append(res[i])

        return new_res

    def threeSum(self, nums):
        result = []
        for i in range(len(nums)):
            # new_nums = [i for i in nums[i+1:] if i not in nums[:i]]
            new_nums = nums[i + 1:]
            tmp = self.twoSum(new_nums, -nums[i])

            # print(i, -nums[i],new_nums,nums[i+1:] )
            if tmp:
                for each in tmp:
                    result.append([nums[i], each[0], each[1]])

        result = self.drop_duplicates(result)
        return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 方便完成不重复的任务，也便于决定两个指针如何移动
        n = len(nums)
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # 使无重复
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while right > left and nums[left] == nums[left + 1]:  # 使无重复
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:  # 使无重复
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result


nums = [2, 7, 11, 15]
nums = [-1, 0, 1, 2, -1, -4]
# target = 9
s = Solution()
[[-1, 0, 1], [-1, -1, 2]]
res = s.threeSum(nums)
print(res)
