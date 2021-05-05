"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


# 我的解法
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # todo 如果我们按照区间的 start 大小排序，那么在这个排序的列表中可以合并的区间一定是连续的。
        intervals = sorted(intervals, key=lambda x: x[0])
        while True:
            if len(intervals) < 2:
                return intervals
            is_outer_continue = False
            is_finished = False
            for i in range(len(intervals) - 1):
                if intervals[i][-1] >= intervals[i + 1][0]:
                    intervals[i] = [min(intervals[i] + intervals[i + 1]), max(intervals[i] + intervals[i + 1])]
                    intervals = intervals[:i + 1] + intervals[i + 2:]
                    is_outer_continue = True
                    break
                if i == len(intervals) - 2:
                    is_finished = True
            if is_outer_continue:
                continue

            if is_finished:
                break

        return intervals


# 比人的解法
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][-1] = max(merged[-1][-1], interval[-1])

        return merged


if __name__ == "__main__":
    a = [[1, 3], [2, 6], [8, 10], [15, 18]]
    a = [[1, 4], [4, 5]]
    a = [[1, 4], [0, 4]]
    a = [[1, 4], [2, 3]]
    a = [[1, 4], [0, 0]]
    s = Solution()
    print(s.merge(intervals=a))
