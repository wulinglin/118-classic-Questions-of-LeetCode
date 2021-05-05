"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

链接：https://leetcode-cn.com/problems/permutations
"""
from typing import List



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []

        def backtrack(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return  # todo

            for i in nums:
                if i not in tmp:
                    backtrack(nums, tmp + [i])  # 纵向

                    # todo 更优雅的写法：append pop => backtrack(nums, tmp+[i])

        backtrack(nums, tmp)
        return res


if __name__ == "__main__":
    s = Solution()
    input = [1, 2, 3]
    print(s.permute(input))
