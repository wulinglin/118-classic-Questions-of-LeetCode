# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
#  你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点
# 。
#
#  示例 1:
#
#
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
#
#
#  注意: 合并必须从两个树的根节点开始。
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#         return t1

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 结点都为空时
        if not t1 and not t2:
            return
        # 只有一个结点为空时
        if not t1:
            return t2
        if not t2:
            return t1

        root = TreeNode(None)
        # 结点重叠时
        root.val = t1.val + t2.val
        # 进行迭代
        # root.right = self.mergeTrees(t1.right if t1, t2.right)
        # root.left = self.mergeTrees(t1.left, t2.left)
        root.left = self.mergeTrees(t1.left if (t1 and t1.left) else None, t2.left if (t2 and t2.left) else None)
        root.right = self.mergeTrees(t1.right if (t1 and t1.right) else None, t2.right if (t2 and t2.right) else None)

        return root

# leetcode submit region end(Prohibit modification and deletion)
