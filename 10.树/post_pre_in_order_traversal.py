class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
A.left, A.right = B, C
B.right = D
C.left, C.right = E, F
E.left = G
F.left, F.right = H, I

A = TreeNode(0)
A.right = TreeNode(-1)
root = A


# 先序


# 用栈不断压入根、左孩子，通过pop来回溯父节点，再访问右孩子。
class Solution:
    """
    先序遍历 中左右
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
            print('***', [i.val for i in stack])
            print('---', seq)
        return seq


class Solution:
    """
    中序遍历 左中右
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


class Solution:
    """
    先序：中左右
    后续：左右中
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


# class Solution:
#     def inorderTraversal(self, root: TreeNode):
#         stack,rst = [root],[]
#         while stack:
#             i = stack.pop()
#             if isinstance(i,TreeNode):
#                 # stack.extend([i.right,i.val,i.left]) ## 中序遍历
#                 stack.extend([i.val,i.right,i.left]) ## 后序遍历
#                 # stack.extend([i.right,i.left,i.val]) ## 先序遍历
#             elif isinstance(i,int):
#                 rst.append(i)
#         return rst
class Solution:
    """
    其核心思想如下：
    使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
    如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
    如果遇到的节点为灰色，则将节点的值输出。

    步骤：
    1.第一个所入节点为root
    2.while stack:
            color, node = stack.pop()
            此时，如果节点颜色为白色：
                 则按照前序、中序、后序的逆顺序将数据压入栈，并且node节点为灰色
            否则：
                 result.append(node.val)
    """

    def inorderTraversal(self, root):
        WHITE, GRAY = 0, 1
        res, stack = [], [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                # 先序
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
                # 中序
                # stack.append((WHITE, node.right))
                # stack.append((GRAY, node))
                # stack.append((WHITE, node.left))
                # # 后序
                # stack.append((GRAY, node))
                # stack.append((WHITE, node.right))
                # stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode):
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if isinstance(node, TreeNode):
                stack.extend([node.right, node.val, node.left])
            elif isinstance(node, int):
                res.append(node)
        return res


# 补充一个层序遍历
class Solution:
    def levelTraversal(self, root: TreeNode) -> List[int]:
        queue,rst = [root],[]
        while queue:
            i = queue.pop(0)
            if isinstance(i,TreeNode):
                queue.extend([i.val,i.left,i.right])
            elif isinstance(i,int):
                rst.append(i)
        return rst


s = Solution()
# print(s.preorderTraversal(root))
print(s.inorderTraversal(root))
# print(s.postorderTraversal(root))
# print(s.levelTraversal(root))
# 先序
res = ['A', 'B', 'D', 'C', 'E', 'G', 'F', 'H', 'I']
# 中序
res = ['B', 'D', 'A', 'G', 'E', 'C', 'H', 'F', 'I']
# 后序
res = ['D', 'B', 'G', 'E', 'H', 'I', 'F', 'C', 'A']
