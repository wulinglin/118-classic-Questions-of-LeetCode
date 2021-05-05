""""
题目
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# hash
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        d = {}
        for i in range(0, n):
            reduction = target - nums[i]
            if i > 0 and nums[i] in d:
                return [d[nums[i]], i]
            d[reduction] = i  # 这个放在这里哈


# list_a = [1,2,3,4]
# list_b = [3,1,2]
# set_c = set(list_a) & set(list_b)
# list_c = list(set_c)
# print(list_c)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def twoSum(nums, target):
            n = len(nums)
            d = {}
            for i in range(0, n):
                reduction = target - nums[i]
                if i > 0 and nums[i] in d:
                    return [d[nums[i]], i]
                d[reduction] = i  # 这个放在这里哈

        def equal(list_a, list_b):
            list_c = set(list_a) & set(list_b)

            return len(list_c) == len(set(list_a))

        def drop_suplicates(lists):
            new_lists = []
            for idx, i in enumerate(lists):
                is_equal = False
                for j in lists[idx + 1:len(lists)]:
                    print(i, j, equal(i, j))
                    if equal(i, j):
                        is_equal = True
                        break
                if not is_equal:
                    new_lists.append(i)
            return new_lists

        m = len(nums)
        res = []
        target = 0
        for j in range(0, m):
            cur_nums = nums[:j] + nums[j + 1:m]
            two_sum_res = twoSum(cur_nums, target - nums[j])
            if two_sum_res:
                res.append([nums[j], cur_nums[two_sum_res[0]], cur_nums[two_sum_res[1]]])
        # print(res, drop_suplicates(res))
        # print(res)
        return drop_suplicates(res)


s = Solution()
nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
# [3,-4,1],,[6,-4,-2]]
# [[-4,-2,6],[-4,0,4],[-4,1,3]]

print(s.threeSum(nums=nums
                 ))
