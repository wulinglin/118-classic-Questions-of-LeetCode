"""
1277. 统计全为 1 的正方形子矩阵

给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
示例 1：

输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释：
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.
示例 2：

输入：matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.
"""


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        import numpy as np
        def is_matrix_all_one(nums):
            if (nums == 1).all():
                return 1
            else:
                return 0
            # return (np.array(nums)==1).all()

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        matrix = np.array(matrix)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[i][j]
                    print(i, j, dp)
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + matrix[i][j]
                    print(i, j, dp)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + matrix[i][j]
                    print(i, j, dp)
                else:

                    cur_num = 0
                    for idx in range(min(i + 1, j + 1)):
                        cur_num += is_matrix_all_one(matrix[i - idx:i + 1, j - idx:j + 1])
                        print(is_matrix_all_one(matrix[i - idx:i + 1, j - idx:j + 1]))
                        print('--', i, j, idx, matrix[i - idx:i + 1, j - idx:j + 1], i - idx, i + 1, j - idx, j + 1)

                        # print(dp)
                    print(i, j, cur_num, dp[i - 1][j], dp[i][j - 1], dp)

                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + cur_num
                    # print(i,j,dp)

        print(dp)
        return dp[-1][-1]


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        import numpy as np

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        matrix = np.array(matrix)
        ans = 0
        for i in range(m):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]

        if matrix[0][0] == 1:
            ans -= 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans += dp[i][j]

        return ans


"""
dp[i][j] = Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1;
"""

matrix = [[0, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 1, 1, 1]]
import numpy as np

s = Solution()
print(np.array(matrix))

s.countSquares(matrix)
