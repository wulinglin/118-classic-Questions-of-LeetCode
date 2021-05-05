# 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
#  说明：
#
#
#  拆分时可以重复使用字典中的单词。
#  你可以假设字典中没有重复的单词。
#
#
#  示例 1：
#
#  输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
#
#
#  示例 2：
#
#  输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
#
#
#  示例 3：
#
#  输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        while s:
            for each in wordDict:
                s = s.replace(each, '')
        if not s:
            return True

        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 初始化 dp
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # 遍历字符串
        for i in range(1, len(s) + 1):
            # j 逐渐划分字符串
            for j in range(i, -1, -1):
                # 判断前缀部分是否为真以及后面剩余部分是否在单词表中
                dp[i] = dp[j] and (s[j:i] in wordDict)
                # 如果为真跳出循环，这里已经判定可以拆分，没必要继续
                if dp[i]:
                    break

        return dp[len(s)]

# leetcode submit region end(Prohibit modification and deletion)
