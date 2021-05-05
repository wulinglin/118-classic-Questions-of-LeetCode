# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
#  说明：
#
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#  示例 1:
#
#  输入: [2,2,1]
# 输出: 1
#
#
#  示例 2:
#
#  输入: [4,1,2,1,2]
# 输出: 4
#  Related Topics 位运算 哈希表
from functools import reduce
from typing import List



"reduce() 函数会对参数序列中元素进行累积。"


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # print(reduce(lambda x, y: x ^ y, nums))
        return reduce(lambda x, y: x ^ y, nums)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            print(i, nums[i], xor, nums[i] ^ xor)
            xor ^= nums[i]
        return xor


"""
异或这招实在是太妙了
print(i, nums[i], xor, nums[i] ^ xor)
0 4 0 4
1 1 4 5
2 2 5 7
3 1 7 6
4 2 6 4
"""

s = Solution()
s.singleNumber([1, 1, 2, 2, 4])
# # leetcode submit region end(Prohibit modification and deletion)
