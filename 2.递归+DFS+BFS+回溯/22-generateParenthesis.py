"""
括号生成：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(p=0, q=0, path=''):
            if len(path) == 2 * n:
                res.append(path)
                return
            if p < n:
                """
                区别在于，
                """
                dfs(p + 1, q, path + '(')

            if q < p:

                dfs(p, q + 1, path + ')')

        dfs()
        return res



s = Solution()
print(s.generateParenthesis(n=3))
