"""
买卖股票最佳时期：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

题解1：
dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：
dp[i] = max(dp[i-1], prices[i]-minprice)

题解2：
如果你学过高等数学，对牛顿莱布尼茨公式有印象的话：
∫f(x)dx==F(b)−F(a)

只不过，在我这里，F() 函数不是连续的，而是离散化的a和b表示数组的下标。但是这不影响我们得出正确的结论。
总结下：区间和可以转换成求差的问题，求差问题，也可以转换成区间和的问题。
在上面的公式中，我们把 F()表示的数组称为前缀和。
最大连续子数组和可以使用动态规划求解， dp[i]表示以 i为结尾的最大连续子数组和，递推公式为：
dp[i] = max(0, dp[i-1])
"""
from typing import List


# 我的
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        nums = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        dp = [0] * (len(prices) - 1)
        for i in range(len(dp)):
            if i == 0:
                dp[i] = max(0, nums[i])
            else:
                dp[i] = max(dp[i - 1] + nums[i], nums[i], 0)
        return max(dp)


# 别人的
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
