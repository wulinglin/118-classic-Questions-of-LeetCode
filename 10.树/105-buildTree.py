"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7] # 中左右
中序遍历 inorder = [9,3,15,20,7] # 左右中
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def buildTree(self, preorder, inorder):

        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            index = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
            root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
            return root
