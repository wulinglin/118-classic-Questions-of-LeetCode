"""给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

输入: "cbbd"
输出: "bb"
"""

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    # 中心扩散法Spread From Center
    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 动态规划法-中心扩散法Spread From Center
    def spread_from_center(self, s: str) -> str:
        if s == s[::-1]:
            return s
        res = s[:1]

        for i in range(len(s)):
            palindrome_odd = self.spread(s=s, left=i, right=i)
            palindrome_even = self.spread(s=s, left=i, right=i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd, palindrome_even, res, key=len)
            print(i, res, palindrome_odd, palindrome_even)
        return res


## 动态规划：
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for i in range(len(s))]
        if not s or len(s) == 1:
            return s
        max_len = 1
        result = s[:1]

        for j in range(len(s)):
            for i in range(len(s)):
                if i <= j:
                    if j == i:
                        dp[i][j] = True
                    elif j == i + 1:
                        dp[i][j] = (s[i] == s[j])
                    else:
                        dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                    if dp[i][j]:
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            result = s[i:j + 1]
        return result


if __name__ == "__main__":
    s = Solution()
    res = s.spread_from_center(s='babad')
    print(res)
    # print(longestPalindrome(s='babad'))
    print(s.spread_from_center(s='acccc'))

    # print('res',longestPalindrome(s='babadddede'))
    # print('res',longestPalindrome(s='cbbd'))
