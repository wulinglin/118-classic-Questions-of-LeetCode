# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。
#
#
#
#  示例：
#
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
#  提示：
#
#
#  3 <= nums.length <= 10^3
#  -10^3 <= nums[i] <= 10^3
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 双指针
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        m = abs(res - target)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(res - target) > abs(temp - target):
                    res = temp
                elif target < temp:
                    r -= 1
                else:
                    l += 1
        return res
