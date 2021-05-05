"""
题目描述：

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
"({())(})"
"({()})()"

考查：栈
    1.拿到一个题首先要考虑有几种情况：
    1)空和奇数个直接排除
    2)剩下偶数个，若第一个就是右括号直接排除，不是右括号再入栈。
    2.画个流程图辅助。
    3.for else的用法。for循环完后执行else语句块，若for中有break，则跳过else。
    4.l[-1]为l的最后一个元素。
"""


# 我的
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '{': '}', '[': ']'}
        # 奇数个排除！
        if len(s) % 2 != 0:
            return False
        if len(s) == 0:
            return True
        if s[0] in [')', ']', '}']:
            return False
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if i != d[stack.pop()]:
                    return False
        return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        # 奇数个排除！
        if len(s) % 2 != 0 or len(s) == 0:
            return False

        for i in s:
            if i in d:
                stack.append(i)
            else:
                # 对称的，对称的话，则第一次出现的反括号一定是最近的正括号
                if i != d[stack.pop()]:
                    return False

        # return True
        return stack == []


in_ = "({()})()"
# in_="({())(})"

s = Solution()
res = s.isValid(in_)
print(res)
