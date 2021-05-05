"""
中序遍历

给定一个二叉树，返回它的中序遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

递归，迭代，莫里斯算法

左中右
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# A, B, C, D = [TreeNode(x) for x in [1, None, 2, 3]]
# A.left, A.right = B, C
# C.left = D
# root=A
A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
A.left, A.right = B, C
B.right = D
C.left, C.right = E, F
E.left = G
F.left, F.right = H, I
root = A


# 递归 # 没懂
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res


# 迭代
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        if not root:
            return []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right  # todo 怎么办怎么都看不懂
        return res


# 先序打印二叉树（递归）
def preOrderTraverse(node):
    if node is None:
        return None
    print(node.val)
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)


# 先序打印二叉树（非递归）
def preOrderTravese(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        node = stack.pop()


s = Solution()
print(s.inorderTraversal(root))
