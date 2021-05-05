# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
#  说明：
#
#
#  字母异位词指字母相同，但排列不同的字符串。
#  不考虑答案输出的顺序。
#
#
#  示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
#  示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#  Related Topics 哈希表

"https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/hua-dong-chuang-kou-tong-yong-si-xiang-jie-jue-zi-/"


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        '''
        解法1：滑动窗口
        '''
        res = []
        window = {}  # 记录窗口中各个字符数量的字典
        needs = {}  # 记录目标字符串中各个字符数量的字典
        for c in p:
            needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息
        print(needs)

        length, limit = len(p), len(s)
        left = right = 0  # 定理两个指针，分别表示窗口的左、右界限

        while right < limit:
            c = s[right]
            if c not in needs:  # 当遇到不需要的字符时
                window.clear()  # 将之前统计的信息全部放弃
                left = right = right + 1  # 从下一位置开始重新统计
            else:
                window[c] = window.get(c, 0) + 1  # 统计窗口内各种字符出现的次数
                if right - left + 1 == length:  # 当窗口大小与目标字符串长度一致时
                    if window == needs:
                        res.append(left)  # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1  # 并将移除的字符数量减一
                    left += 1  # left右移
                right += 1  # right右移
        return res

# leetcode submit region end(Prohibit modification and deletion)
