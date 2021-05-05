# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#  示例：
#
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        ans = node  # TODO ，为什么？
        """
        这里只能是ans = node; 结尾return ans.next;
        如果我这里写ans=node.next；结尾return ans就不行.
        为什么？
        """

        flag = 0
        while l1 or l2:
            if l1 and l2:
                cursum = l1.val + l2.val + flag
                l1 = l1.next
                l2 = l2.next
            elif l1:
                cursum = l1.val + flag
                l1 = l1.next
            elif l2:
                cursum = l2.val + flag
                l2 = l2.next

            if cursum > 9:
                node.next = ListNode(cursum % 10)
                flag = 1
            else:
                node.next = ListNode(cursum)
                flag = 0
            node = node.next
        if flag:
            node.next = ListNode(flag)
        return ans.next

# leetcode submit region end(Prohibit modification and deletion)
