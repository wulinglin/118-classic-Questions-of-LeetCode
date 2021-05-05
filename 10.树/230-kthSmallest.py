"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

先序遍历：在第一次遍历到节点时就执行操作，一般只是想遍历执行操作（或输出结果）可选用先序遍历；
中序遍历：对于二分搜索树，中序遍历的操作顺序（或输出结果顺序）是符合从小到大（或从大到小）顺序的，故要遍历输出排序好的结果需要使用中序遍历
后序遍历：后续遍历的特点是执行操作时，肯定已经遍历过该节点的左右子节点，故适用于要进行破坏性操作的情况，比如删除所有节点
"""


# from base.tree import Btree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        # TODO 中序遍历：对于二分搜索树，中序遍历的操作顺序（或输出结果顺序）是符合从小到大（或从大到小）顺序的，故要遍历输出排序好的结果需要使用中序遍历
        res, stack = [], []
        while root or stack:
            # stack.append(root)
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = root.right

        return res[k - 1]


class Solution:
    def kthSmallest(self, root: TreeNode, k):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.val, node.left])
            elif isinstance(node, int):
                res.append(node)
        return res[k - 1]




s = Solution()
