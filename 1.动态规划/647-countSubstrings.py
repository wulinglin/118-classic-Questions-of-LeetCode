# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#
#
#
#  示例 1：
#
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#
#
#  示例 2：
#
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
#
#  提示：
#
#
#  输入的字符串长度不会超过 1000 。
#
#  Related Topics 字符串 动态规划
"""
动态规划的思想是，我们先确定所有的回文，即 string[start:end]是回文. 当我们要确定string[i:j] 是不是回文的时候，要确定：

string[i] 等于 string[j]吗?
string[i+1:j-1]是回文吗?
单个字符是回文；两个连续字符如果相等是回文；如果有3个以上的字符，需要两头相等并且去掉首尾之后依然是回文。
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += 1
            # 回文长度是奇数的情况
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            # 回文长度是偶数的情况
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count

# leetcode submit region end(Prohibit modification and deletion)
