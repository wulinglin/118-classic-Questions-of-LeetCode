"""长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
 如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

https://zhuanlan.zhihu.com/p/61564531
"""


# 第一个版本：超时
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import copy
        left, right = 0, 0
        optim = len(nums) + 1
        if len(nums) == 0:
            return 0
        while left < len(nums):
            while right < len(nums):
                right += 1
                if sum(nums[left:right]) >= s:
                    optim = min(optim, len(nums[left:right]))
                    break
                if len(nums[left:right]) > optim - 1:
                    break

            left += 1
            right = copy.deepcopy(left)
        if optim > len(nums):
            optim = 0

        return optim


class Solution(object):
    """
    初始化窗口端点L，R，一般L为0，R为1
    初始化最优值
    while R < len(Array): #TODO 怎么不是L< len(Array)
        while R < len(Array):
            R += 1              #移动右端点
            if R < len(Array):
                更新状态
            if 状态满足条件:
                可选的更新最优值的位置
                break           #一旦满足条件即跳出
        if R == len(Array):     # 若循环是由于移动到数组末尾结束，则停止整个程序。因为之后已经不再有可能的解
            break
        while L < R:
            更新状态    # 移动左端点，需要更新状态
            L += 1
            if 状态满足条件：
                可选的更新最优值的位置
            else：  # 一旦窗口所在区间不再满足条件即跳出，去移动右端点
                break
        可选的对于L，R端点的后续处理
    return 最优值
    """

    pass


class Solution(object):
    def minSubArrayLen(self, s: int, nums):
        summation = 0
        left, right = 0, -1  # WHY -1
        optim = len(nums) + 1
        while left < len(nums):  # todo why  while right < len(nums):
            while right < len(nums):
                right += 1
                if right < len(nums):
                    summation += nums[right]  # 因为是-1所以才能summation += nums[right]
                if summation >= s:
                    optim = min(optim, right - left + 1)
                    break

            if right == len(nums):
                break

            while left < right:
                summation -= nums[left]
                left += 1
                print(left, right)
                if summation >= s:
                    optim = min(optim, right - left + 1)
                else:
                    break
        return optim if optim != len(nums) + 1 else 0


class Solution(object):
    def minSubArrayLen(self, s: int, nums):
        if len(nums) == 0 or sum(nums) < s:
            return 0

        left, right = 0, -1
        optim = len(nums) + 1
        summation = 0
        while left < len(nums):
            while right < len(nums):
                if summation < s and right + 1 < len(nums):
                    right += 1
                    summation += nums[right]
                elif summation >= s:
                    # print('-' * 3, left, right, summation, optim, right - left, min(optim, right - left + 1))
                    optim = min(optim, right - left + 1)
                    break
                else:
                    break

            summation -= nums[left]
            left += 1
        return optim


s = 7
nums = [2, 3, 1, 2, 4, 3]
# s = 100
# nums = []
# s = 4
# nums = [1, 4, 4]
# s = 3
# nums = [1, 1]
# print(nums)
a = Solution()
print(a.minSubArrayLen(s, nums))
