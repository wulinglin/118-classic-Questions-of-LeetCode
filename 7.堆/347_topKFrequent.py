"""347. 前 K 个高频元素

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
"""


# 排序
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter  # todo Counter
        count = Counter(nums)
        res = sorted(count.items(), key=lambda x: x[1], reverse=True)  # todo items(),  key=
        print(res)
        return [i[0] for i in res[:k]]


# 堆
class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


c


class Solution(object):
    def topKFrequent(self, words, k):
        import collections
        import heapq
        count = collections.Counter(words)

        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        print(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
a = Solution()
print(a.topKFrequent(nums, k))
