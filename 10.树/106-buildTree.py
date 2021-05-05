"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7] #左中右
后序遍历 postorder = [9,15,7,20,3] #左右中
1
2
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
1
2
3
4
5
————————————————
原文链接：https://blog.csdn.net/Forlogen/article/details/105159853
"""
from typing import List


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        else:
            root = TreeNode(postorder[-1])
            index = inorder.index(root.val)

            root.left = self.buildTree(inorder[:index], postorder[: index])
            root.right = self.buildTree(inorder[index + 1:], postorder[index: -1])

            return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
s = Solution()
res = s.buildTree(inorder, postorder)
print(res)
