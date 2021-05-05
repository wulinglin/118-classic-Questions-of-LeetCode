# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。
#
#
#
#  示例：
#
#  输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"
#
#
#
#  提示：
#
#
#  如果 S 中不存这样的子串，则返回空字符串 ""。
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:  # 虽然D不在need但是默认为0
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


s = Solution()
S = "ADOBECODEBANC"
T = "ABC"
s.minWindow(S, T)

# leetcode submit region end(Prohibit modification and deletion)
