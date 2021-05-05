"""堆成二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

"""


def a(root):
    if not root:
        return True

    def dfs(left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        # if root.left or root.right:
        if left.val != right.val:
            return False
        return


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(left, right):
            # 递归的终止条件是两个节点都为空
            # 或者两个节点中有一个为空
            # 或者两个节点的值不相等
            if not (left or right):
                return True  # todo 这是两个都为none
            if not (left and right):
                return False  # todo 这是其中一个为none
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        # 用递归函数，比较左节点，右节点
        return dfs(root.left, root.right)
