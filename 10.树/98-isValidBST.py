"""
98. 验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorderTravelsal(root):
            res, stack = [], [root]
            while stack:
                node = stack.pop()
                if isinstance(node, TreeNode):
                    stack.extend([node.right, node.val, node.left])
                elif isinstance(node, int):
                    res.append(node)
            return res

        inorder_res = inorderTravelsal(root)
        print(inorder_res)
        if len(inorder_res) <= 1:
            return True
        for i in range(1, len(inorder_res)):
            if inorder_res[i - 1] >= inorder_res[i]:
                return False
        return True


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True  # 递归结束条件

            val = node.val
            if val <= lower or val >= upper:  # 如果触犯了搜索树的原则直接返回False
                return False
            if not helper(node.right, val, upper):  # 判断右子树是否都大于当前节点值
                return False
            if not helper(node.left, lower, val):  # 判断左子树是否都小于当前节点值
                return False
            return True  # 如果都通过了就代表没问题

        return helper(root)
