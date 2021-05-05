"""
103. 二叉树的锯齿形层次遍历
难度中等
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def helper(root, level):
            if level == len(res):
                res.append([])

            res[level].append(root.val)

            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, level=0)

        temp = []
        for i in range(len(res)):
            if i % 2 == 0:
                temp.append(res[i])
            else:
                temp.append(res[i][::-1])

        return temp
