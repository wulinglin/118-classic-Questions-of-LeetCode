"""
Subtree of Another Tree（判断一棵树是不是另外一棵树的子树）
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:

给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值

"""
from base.tree import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

    def isSubtree(self, s, t):
        # print(self.isSameTree(s, t))
        if self.isSameTree(s, t):
            return True
        if s.left:
            if self.isSubtree(s.left, t):
                return True

        if s.right:
            if self.isSubtree(s.right, t):
                return True
        return False
