"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def ishuiwen(s):
            return s == s[::-1]

        def dfs(l, start, end):
            if len(''.join(l)) == len(s):
                res.append(l)
                return
            cur = start
            while cur < len(s):
                if ishuiwen(s[start:cur + 1]):
                    dfs(l + [s[start:cur + 1]], cur + 1, end)
                cur += 1
                # else:
                #     break

        dfs(l=[], start=0, end=len(s))
        return res


s = Solution()
s_ = 'aab'
s_ = 'efe'
res = s.partition(s_)
print(res)
