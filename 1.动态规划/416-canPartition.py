# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#  注意:
#
#
#  每个数组中的元素不会超过 100
#  数组的大小不会超过 200
#
#
#  示例 1:
#
#  输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
#
#
#
#  示例 2:
#
#  输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
#
#
#  Related Topics 动态规划
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1 or len(nums) < 2:
            return False

        half = sum(nums) // 2
        nums.sort(reverse=True)
        if nums[0] > half:
            return False

        @lru_cache(None)  # 不加就超时了呢
        def dfs(target, i):
            if target == nums[i]:
                return True

            if target > nums[i]:
                for j in range(i + 1, len(nums)):
                    if dfs(target - nums[i], j):
                        return True
            return False

        return dfs(half, 0)


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# from collections import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        sum_ = sum(nums)
        if sum_ % 2 != 0 or len(nums) < 2:
            return False

        per_sum = sum_ / 2
        if nums[0] > per_sum:
            return False
        n = len(nums)

        # TODO以下这种写法最大的问题在于会有重复计算
        # @lru_cache(None) # 不加就超时了呢
        # def dfs(cursum, loc):
        #     # print(cursum, loc,per_sum, per_sum==cursum)
        #     if cursum == per_sum:
        #         return True
        #     if loc>n:
        #         return False
        #     for i in range(loc, n):
        #         # cursum=cursum + nums[i]
        #         if cursum + nums[i]>per_sum:
        #             if dfs(cursum, loc + 1):
        #                 return True
        #         else:
        #             if dfs(cursum+nums[i], loc+1):
        #                 return True
        #         # if dfs(cursum, loc+1):
        #         #     return True
        #     return False
        def dfs(cursum, loc):
            if cursum + nums[loc] == per_sum:
                return True
            if loc >= n:
                return False

            if cursum + nums[loc] < per_sum:
                for i in range(loc + 1, n):
                    if dfs(cursum + nums[i], i):
                        return True
            return False

        return dfs(cursum=0, loc=0)


# nums=[1, 5, 11, 5]
# nums=[2,2,1,1]
nums = [2, 2, 3, 5]
s = Solution()
print(s.canPartition(nums))

# leetcode submit region end(Prohibit modification and deletion)
