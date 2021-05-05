# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 回溯算法


"""
    方法二：递归
    f([1,2]) = [[], [1,2], [2], [1]];
    f([1,2,3]) = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    f([1,2,3])是在f([1,2])的元素基础上，对每个元素多加一个3

    """


class Solution(object):
    def subsets(self, nums):
        if nums == []:
            return [[]]
        return self.subsets(nums[:-1]) + [i + [nums[-1]] for i in self.subsets(nums[:-1])]


"""动态规划
跟上面递归的想法类似，就是找出当前的结果跟前一个结果的关系：
dp[i] = dp[i-1] + [each+[nums[i]] for each in dp[i-1]]
"""


class Solution(object):
    def subsets(self, nums):
        dp = [[]]
        for i in range(len(nums)):
            dp = dp + [each + [nums[i]] for each in dp]
        return dp


s = Solution()
s.subsets([1, 2, 3])
