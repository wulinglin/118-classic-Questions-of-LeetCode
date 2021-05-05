"""
322. 零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

w v
1 1
2 1
5 1

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

总金额就是背包容量，硬币就是物品，可以表示为，物品（vi--coins[i], wi--1(价值就是数量，每个硬币的数量就是1)）

定义状态：dp[i][j]:当考虑放入第i枚硬币时，所凑成金额j时的最小硬币数。仿照上面，状态转移方程为：dp[i][j]=Min(dp[i-1][j],dp[i][j-conins[i]]+1)

现在需要思考初始条件了，求的是最小值，那么我们在最开始时，需要将值设为最大，同时dp[0]
"""


class Solution:
    def coninChange(self, coins, amount):
        v, w, c = coins, [1] * len(coins), amount
        dp = [0] + [c + 1] * c
        for i in range(0, len(v)):
            for j in range(0, c + 1):
                if j - v[i] >= 0:
                    dp[j] = min(dp[j], dp[j - v[i]] + 1)
        if dp[c] == c + 1:
            return -1

        return dp[-1]


coins = [1, 2, 5]
amount = 11
coins = [2]
amount = 2
coins = [3]
amount = 2
amount =2
s = Solution()
res = s.coninChange(coins, amount)
print(res)
