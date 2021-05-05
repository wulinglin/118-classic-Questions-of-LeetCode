"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):

        if n == 0:
            return []
        s = [_ + 1 for _ in range(n)]
        return self.helper(s)

    def helper(self, s):
        if len(s) == 1:
            return [TreeNode(s[0])]
        if s == []:
            return [None]
        l = []
        for i in range(len(s)):
            for a in self.helper(s[:i]):
                for b in self.helper(s[i + 1:]):
                    root = TreeNode(s[i])
                    root.left = a
                    root.right = b
                    l.append(root)

        return l
