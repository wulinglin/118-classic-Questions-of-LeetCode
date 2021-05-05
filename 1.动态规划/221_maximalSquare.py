"""
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
示例:

输入:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        import numpy as np
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        matrix = np.array(matrix)
        ans_max = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            ans_max = max(ans_max, dp[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            ans_max = max(ans_max, dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans_max = max(ans_max, dp[i][j])

        return ans_max ** 2


matrix = [[0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 1, 1, 1]]
matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]
import numpy as np

s = Solution()
print(np.array(matrix))

s.maximalSquare(matrix)
"""
要找到二维矩阵中，只包含 1 的最大正方形，我们可以用动态规划解决。用 dp[i][j] 表示直到 (i, j) 位置的可以包含最大正方形的边长，
注意这里的正方形需要包含 (i, j) 位置。

在矩形左侧和上边界，如果 matrix[i][j]=='1'，有 dp[0][j]==dp[i][0]==1，即能构成的最大正方形的边长为 1。

而对于更一般的情况：

1、如果 matrix[i][j]=='0'，显然 dp[i][j]==0。
2、如果 matrix[i][j]=='1'，状态转移方程为：dp[i][j]=min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1，即 (i, j) 位置的值被其左侧、上侧、左上侧的值所限制。
"""
