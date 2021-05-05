"""滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums =
[1,3,-1,-3,5,3,6,7]
, 和 k = 3
输出:[3,3,5,5,6,7]

# todo  哪里有双端队列？
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        if len(nums) <= k:
            res.append(max(nums))
            return res

        for i in range(len(nums) - k + 1):
            print(nums[i:i + k])
            res.append(max(nums[i:i + k]))
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
res = s.maxSlidingWindow(nums, k)
print(res)
