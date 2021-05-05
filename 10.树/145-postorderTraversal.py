"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
左右中
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
# 先序
res = ['A', 'B', 'D', 'C', 'E', 'G', 'F', 'H', 'I']
# 后序
res = ['D', 'B', 'G', 'E', 'H', 'I', 'F', 'C', 'A']


class Solution:
    """
    先序：根左右
    后续：左右根
    即把先序顺序中的 ‘根左右’转换为‘根右左’，然后反过来就变成了‘左右根’。
    """

    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = []
        seq = []
        output = []
        while root or len(stack) != 0:
            if root:
                seq.append(root.val)
                stack.append(root)
                root = root.right  # 这从left变成了 right
            else:
                root = stack.pop()
                root = root.left  # 这从right变成了 left

        while seq:  # 后序遍历 是 将先序遍历的反过来
            output.append(seq.pop())

        return output


s = Solution()
print(s.postorderTraversal(root))


class Solution:
    """
    先序遍历
    """

    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        stack = []
        seq = []  # 记录先序访问序列
        while root or len(stack) != 0:
            if root:
                seq.append(root.val)  # 先访问根节点
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()  # 回溯至父节点
                root = root.right
        return seq


class Solution:
    """
    中序遍历
    """

    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = []
        seq = []
        output = []
        while root or len(stack) != 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                seq.append(root.val)  # 左孩子先pop出来，再pop根节点
                root = root.right

        return seq
