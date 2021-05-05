"""
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

"""


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        print(longest_streak, current_streak)
        return max(longest_streak, current_streak)


class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {x: False for x in num}  # False means not visited
        maxLen = -1
        for i in dict:
            if dict[i] == False:
                curr = i + 1
                lenright = 0
                while curr in dict:
                    lenright += 1
                    dict[curr] = True
                    curr += 1
                curr = i - 1
                lenleft = 0
                while curr in dict:
                    lenleft += 1
                    dict[curr] = True;
                    curr -= 1
                maxLen = max(maxLen, lenleft + 1 + lenright)
        return maxLen


numCourses, prerequisites = 2, [[1, 0], [0, 1]]
s = Solution()
nums = [100, 4, 200, 1, 3, 2]
res = s.longestConsecutive(nums)
print(res)
