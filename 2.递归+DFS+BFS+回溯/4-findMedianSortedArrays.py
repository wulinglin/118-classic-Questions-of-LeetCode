"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
注意：n为偶数的时候，中位数是下标是（n/2+n/2+1)/2；奇数的时候下标为（n+1)/2

nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

困难难题！
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # print(nums1, nums2)
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2  # 这里要减去1哦！

        def get_k(nums1, nums2, k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                new_index1 = min(index1 + k // 2 - 1, m - 1)
                new_index2 = min(index2 + k // 2 - 1, n - 1)
                if nums1[new_index1] <= nums2[new_index2]:
                    k = k - (new_index1 - index1 + 1)
                    index1 = new_index1 + 1
                else:
                    k = k - (new_index2 - index2 + 1)
                    index2 = new_index2 + 1

        if (m + n) % 2 != 0:
            return get_k(nums1, nums2, mid + 1)
        else:
            return (get_k(nums1, nums2, mid) + get_k(nums1, nums2, mid + 1)) / 2


s = Solution()
nums1 = [1, 3]
nums2 = [2]

# nums1 = [1, 3]
# nums2 = [2,2]
nums1 = [1, 2]
nums2 = [3, 4]
# # 预期结果 2.5 ?
res = s.findMedianSortedArrays(nums1, nums2)
# print(res)
# r=findMedianSortedArrays(nums1, nums2)
# print(r)
