"""
33. 搜索旋转排序数组

假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 二分搜索查找旋转的节点：即寻找最小值
        def find_minimum_idx(nums):
            min_, max_ = 0, len(nums)
            while True:
                mid_ = (min_ + max_) // 2
                if mid_ - 1 >= 0 and min_ + 1 < len(nums):
                    if nums[mid_ - 1] > nums[mid_] and nums[mid_ + 1] > nums[mid_]:
                        return mid_
                    elif nums[0] < nums[mid_]:
                        min_ = mid_ + 1
                    elif nums[-1] > nums[mid_]:
                        max_ = mid_ - 1
                else:
                    return mid_

        # 二分查找寻找值
        def binary_search(nums, target):
            min_, max_ = 0, len(nums)
            while True:
                mid_ = (min_ + max_) // 2
                if nums[mid_] == target:
                    return mid_
                elif target > nums[mid_]:
                    min_ = mid_ + 1
                elif target < nums[mid_]:
                    max_ = mid_ - 1
                if max_ < 0 or min_ > len(nums) - 1 or max_ < min_:
                    return
                # print(min_,max_,mid_)

        mid_idx = find_minimum_idx(nums)
        new_nums = nums[-mid_idx + 1:] + nums[:mid_idx]

        idx = binary_search(new_nums, target)
        if not idx:
            return -1
        if idx > len(nums) - mid_idx + 1:
            return idx - (len(nums) - mid_idx + 1)
        else:
            return mid_idx + idx


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] <= nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# target=3
s = Solution()
print(s.search(nums, target))
