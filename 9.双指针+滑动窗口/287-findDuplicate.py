# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
# 可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。
#
#  示例 1:
#
#  输入: [1,3,4,2,2]
# 输出: 2
#
#
#  示例 2:
#
#  输入: [3,1,3,4,2]
# 输出: 3
#
#
#  说明：
#
#
#  不能更改原数组（假设数组是只读的）。
#  只能使用额外的 O(1) 的空间。
#  时间复杂度小于 O(n2) 。
#  数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#  Related Topics 数组 双指针 二分查找
"""
既然是对某个数的定位，我们想到是不是可以用二分法，但是和传统二分不一样的是，我们对要定位的“数”做二分，
而不是对数组的索引做二分。要定位的“数”根据题意在 1 和 n 之间，每一次二分都可以将搜索区间缩小一半。

以 [1, 2, 2, 3, 4, 5, 6, 7] 为例，一共有 8 个数，每个数都在 1 和 7 之间。1 和 7 的中位数是 4，
遍历整个数组，统计小于 4 的整数的个数，至多应该为 3 个，如果超过 3 个就说明重复的数存在于区间 [1,4) （注意：左闭右开）中；

否则，重复的数存在于区间 [4,7]（注意：左右都是闭）中。这里小于 4 的整数有 4 个（它们是 1, 2, 2, 3），
因此砍掉右半区间，连中位数也砍掉。

以此类推，最后区间越来越小，直到变成 1 个整数，这个整数就是我们要找的重复的数，时间复杂度是 [公式] 。


"""

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# 我的方法。先排序，已经更改了原数组，pass
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


# o（n2) 超时
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] == nums[j]:
                        return nums[i]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def count(nums, start, end):
            c = 0
            for i in nums:
                if i > start and i <= end:
                    c += 1
            return c

        def helper(nums, start, end):
            # 这里比较重要的点在于：如果end-start<=1，
            # 那 mid = start + (end - start) // 2这个方法得到的结果会是0.那start和mid就是同一个值了
            if end - start <= 1:
                mid = end
            else:
                mid = start + (end - start) // 2

            c = count(nums, start, mid)
            # print("**",start, end, mid, c)
            if mid - start <= 1 and c >= 2:
                return mid
            elif c > mid - start:  # 说明重复再0-mid(包尾不包头)
                start, end = start, mid
                return helper(nums, start, end)
            else:  # 否则说明在Mid到n（包尾不包头）这个区间
                start, end = mid, end
                return helper(nums, start, end)

        n = len(nums)
        start, end = 0, n
        return helper(nums, start, end)


s = Solution()
nums = [3, 1, 3, 4, 2]
# nums=[1,3,4,2,2]

print(s.findDuplicate(nums=nums))
# leetcode submit region end(Prohibit modification and deletion)
