"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

解析：
动态规划问题：
(1)位于第一行第一列的时候数据为1，（2）其他情况的动态转移方程为：dp[i][j]=dp[i-1][j]+dp[i][j-1]
"""


class Solution:
    "时间复杂度：O(m*n)O(m∗n); 空间复杂度：O(m * n)O(m∗n)"

    def uniquePaths(self, m: int, n: int) -> int:
        "因为要根据第一行第一列推后面的，所以需要先设定第一行第一列的数值"
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    "优化1：空间复杂度 O(2n)"

    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]


class Solution:
    "优化2：空间复杂度 O(n)"

    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


s = Solution()
res = s.uniquePaths(3, 4)
print(res)
