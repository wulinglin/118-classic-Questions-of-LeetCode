# Definition for singly-linked list.
"""
Remove Nth Node From End of List（删除链表倒数第n个节点）
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        特殊情况两种：第一种是总长为1或者0，那么删掉以后就为空了；第二种情况是删除的是第一个数据，顺序数下来n为0，则遍历即可
        常规情况：删除的不是第一个数字，则n为n-1..
        """
        m = 0
        root = head
        while root:
            root = root.next
            m += 1

        n = m - n
        i = 0
        res_list = []
        if m == 1 or m == 0:
            return
        if n == 0:
            head = head.next
            n = m

        while i < m and head:
            res_list.append(head.val)
            if i == n - 1 and head.next:
                head = head.next.next
                i += 2
            else:

                head = head.next
                i += 1

        if len(res_list) < 1:
            return
        node = ListNode(res_list[0])
        curr = node
        for i in res_list[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return node


class Solution:
    """
    1.定义一个头结点，指向链表的第一个结点（不再像1.0版一样计算链表长度）
    2.快慢指针指向头结点
    3.快指针先走n步
    4.快慢指针一起走，直到快指针走到链表尾
    5.慢指针后一位连接为其后一位的后一位（实现截断连接）
    6.返回头结点的后一位结点。
    # 总结：这个方法的优势在于，不需要知道长度m,先走了n步，继续走，走到结尾那就是m-n的步数
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode(None)
        node.next = head
        first, slow = node, node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        return node.next


n = 2
# l=[2,3,4,5]
l = [2, 3, 4, 5]
# l = [5]
# l=[]
head = ListNode(1)
curr = head
for i in l:
    curr.next = ListNode(i)
    curr = curr.next
curr.next = ListNode(None)

s = Solution()
s.removeNthFromEnd(head, n)
