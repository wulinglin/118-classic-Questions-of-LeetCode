"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

题解：
转移方程： dp[i][j]=dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]
空间优化： dp[j]=dp[j-nums[i]]+dp[j+nums[i]]

#todo 待自己完善
"""


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # 如果 nums 的总和都小于 S，肯定是不行的
        # 如果求出的容量 V 是一个浮点数也不符合要求
        if (sum(nums) + S) % 2 != 0 or sum(nums) < S:
            return 0
        # 求背包容量
        V = (sum(nums) + S) // 2
        # dp[i] 表示此时背包容量为 i
        dp = [0] * (V + 1)
        # 为什么 dp[0] 取 1 ？ 因为当背包容量为 0 时，
        # 显然我们不需要取任何数到背包即满足条件，所以可行解为 1
        dp[0] = 1
        for num in nums:
            i = V
            while i >= num:
                # dp[i] 的解法数为自身加上dp[i-num]的解法数
                # 这里为什么会如此，可以参考斐波那契数列
                # 这里我可以不放 num 进背包，解法数为 dp[i]
                # 将 num 放进背包，解法数为 dp[i-num]
                # 所以此时的总解法数为 二者和
                dp[i] = dp[i] + dp[i - num]
                i -= 1  # 背包容量减 1
        return dp[V]
