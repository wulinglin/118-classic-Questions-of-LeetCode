"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


"""


class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return result

        def helper(root, level):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, level=0)
        return result

    def rightSideView(self, root):
        level_result = self.levelOrder(root)
        return [i[-1] for i in level_result]
