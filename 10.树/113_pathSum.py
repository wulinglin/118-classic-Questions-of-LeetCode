# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
#
#  返回:
#
#  [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from post_pre_in_order_traversal import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(cursum, node, l):
            if not node:
                return

            tmp_sum = cursum + node.val
            if tmp_sum == sum and not node.left and not node.right:
                res.append(l + [node.val])
                return
            # elif tmp_sum != sum: # todo 不能加这句!超级重要 ！！！
            dfs(tmp_sum, node.left, l + [node.val])
            dfs(tmp_sum, node.right, l + [node.val])

        dfs(cursum=0, node=root, l=[])
        return res
