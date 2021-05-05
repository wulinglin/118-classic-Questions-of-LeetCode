"""34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


# 自己写的：超时
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        min_, max_ = 0, len(nums)

        while True:
            mid_ = (min_ + max_) // 2
            print(mid_)
            if nums[mid_] == target:
                start = mid_
                end = mid_
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                return start, end
            elif target > nums[mid_]:
                min_ = mid_ + 1
            elif target < nums[mid_]:
                max_ = mid_ - 1
            if max_ < 0 or min_ > len(nums) - 1:
                return [-1, -1]


class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > target or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        print('--------')
        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


nums = [5, 7, 7, 8, 8, 10]
target = 8
s = Solution()
print(s.searchRange(nums, target))
