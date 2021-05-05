"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 暴力解法：双层递归,核心在于：
# 每个node都要计算以它作为起点往下是否有path --> 这是一层递归
# 在考虑当前点为起点往下有没有path的时候，它的path可以往左也可以往右，于是要综合考虑 --> 这是另一层递归

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        '''如果没有根节点，整个返回值应该为0，没有路径'''
        if not root:
            return 0
        '''
        self.dfs(root, sum)：这个方法是判断以当前点为起点往下是否有path，也就是path的数量，返回值应该是0或1
        self.pathSum(root.left, sum)：对于左节点我依然要考虑以它为起点往下判断
        self.pathSum(root.right, sum)：同上，于是，此时的sum是不变化的，仍然为初始值
        '''

        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, root, curr_sum):
        if not root:
            return 0
        '''每一次都要减去当前层的节点值'''

        curr_sum -= root.val
        '''
       (1 if path==0 else 0)：说明找到了路径
       self.dfs(root.left, path) self.dfs(root.right, path)：
         此时path更新过，这是因为当前点既可以往左走找path，也可以往右走，是或的关系，只要有一边找到了路径，最终结果都会为1
        '''
        return (1 if curr_sum == 0 else 0) + self.dfs(root.left, curr_sum) + \
               self.dfs(root.right, curr_sum)


a, b, c, d, e = [TreeNode(x) for x in [1, 2, 3, 4, 5]]
a.right = b
b.right = c
c.right = d
d.right = e

# [1,null,2,null,3,null,4,null,5]
s = Solution()
print(s.pathSum(root=a, sum=3))
