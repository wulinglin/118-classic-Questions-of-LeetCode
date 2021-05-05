"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

中左右
"""


# https://blog.csdn.net/weixin_36677127/article/details/82284909

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
res = ['A', 'B', 'D', 'C', 'E', 'G', 'F', 'H', 'I']


class Solution:
    def preorderTraversal(self, root):
        "先序遍历：中-》左-》右"
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                # 注意压入栈的顺序,先压入右孩子，再压入左孩子
                stack.append(node.right)
                stack.append(node.left)
            print([i.val for i in stack if i])
        return res


s = Solution()
print(s.preorderTraversal(root))
