"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


class Solution:
    def Permutation(self, ss):
        result = []

        def helper(ss, tmp):
            if len(tmp) == len(ss):
                result.append(tmp)
                return

            for i in range(len(ss)):
                if ss[i] not in tmp:
                    helper(ss, tmp + [ss[i]])

        helper(ss, [])
        return result


s = Solution()
ss = 'abc'
res = s.Permutation(ss)
print(res)
