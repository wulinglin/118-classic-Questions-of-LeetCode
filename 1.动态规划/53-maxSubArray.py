"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


思路：
设 f[x] 为以 a[x] 终止且包含 a[x] 的最大序列的和，有：
   f[1] = a[1];
   f[x+1] = max(f[x] ,f[x] + a[x+1]）
那么最大子序列的和就是 f[1] .. f[n] 中最大的一个

首先对数组进行遍历，当前最大连续子序列和为sum，结果为results
如果sum > 0，则说明sum对结果有增益效果，则sum保留并加上当前遍历数字
如果sum <= 0，则说明sum对结果无增益效果，需要舍弃，则sum直接更新为当前遍历数字
每次比较sum 和 results的大小，将最大值置为results，遍历结束后返回结果results
时间复杂度为O（n）
"""


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        dp = [nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            # 先求当前位置最大和，
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]

            # 再求全局最大和
            max_sum = max(dp[i], max_sum)
        return max_sum


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
