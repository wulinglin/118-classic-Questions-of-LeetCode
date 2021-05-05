# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# root = [5,3,6,2,4,null,7]
a, b, c, d, e, f = [TreeNode(i) for i in [5, 3, 6, 2, 4, 7]]
a.left, a.right = b, c
b.left, b.right = d, e
c.right = f

root = a

"""
算法：

如果 key > root.val，说明要删除的节点在右子树，root.right = deleteNode(root.right, key)。
如果 key < root.val，说明要删除的节点在左子树，root.left = deleteNode(root.left, key)。
如果 key == root.val，则该节点就是我们要删除的节点，则：
如果该节点是叶子节点，则直接删除它：root = null。
如果该节点不是叶子节点且有右节点，则用它的后继节点的值替代 root.val = successor.val，然后删除后继节点。
如果该节点不是叶子节点且只有左节点，则用它的前驱节点的值替代 root.val = predecessor.val，然后删除前驱节点。
返回 root。
"""


class Solution:
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root, key: int):
        if not root:
            return None

        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
