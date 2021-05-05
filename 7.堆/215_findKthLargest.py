"""数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


"""


# 堆
class Solution:
    """
    方法一：堆
    思路是创建一个大顶堆，将所有数组中的元素加入堆中，并保持堆的大小小于等于 k。这样，堆中就保留了前 k 个最大的元素。这样，堆顶的元素就是正确答案。
    像大小为 k 的堆中添加元素的时间复杂度为 {O}(\log k)O(logk)，我们将重复该操作 N 次，故总时间复杂度为 {O}(N \log k)O(Nlogk)。
    在 Python 的 heapq 库中有一个 nlargest 方法，具有同样的时间复杂度，能将代码简化到只有一行。
    本方法优化了时间复杂度，但需要 {O}(k)O(k) 的空间复杂度。
    """

    def findKthLargest(self, nums, k):
        import heapq
        return heapq.nlargest(k, nums)[-1]


# 排序
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sort_nums = sorted(nums, reverse=True)
        idx = 0
        for i in sort_nums:

            idx += 1
            if idx == k:
                return i
