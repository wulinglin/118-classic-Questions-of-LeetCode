# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#  示例 1：
#
#  输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#
#
#
#  提示：
#
#
#  1 <= k <= len(nums) <= 16
#  0 < nums[i] < 10000
#
#  Related Topics 递归 动态规划


from typing import List


class Solution:
    # leetcode submit region begin(Prohibit modification and deletion)
    class Solution:
        def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
            per_sum = sum(nums) / k
            nums.sort(reverse=True)
            if sum(nums) % k != 0:
                return False

            visited = [0] * len(nums)

            def dfs(start, cursum, k, visited):
                if k == 0:
                    return True

                if cursum == per_sum:
                    return dfs(0, 0, k - 1, visited)  # todo dfs(0,0, k-1, visited) vs return dfs(0,0, k-1, visited)
                elif cursum > per_sum:
                    return False
                for i in range(start, len(nums)):
                    if not visited[i] and cursum + nums[i] <= per_sum:
                        visited[i] = 1
                        if dfs(i + 1, cursum + nums[i], k, visited):  # todo
                            return True
                        visited[i] = 0  # todo 回溯

            res = dfs(start=0, cursum=0, k=k, visited=visited)
            return res if res else False


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
s = Solution()
print(s.canPartitionKSubsets(nums, k))
