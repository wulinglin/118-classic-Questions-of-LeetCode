"Write a program to find the node at which the intersection of two singly linked lists begins."
from base.linklist import ListNode

l = [9, 1, 2, 4]
# l = [5]
heada = ListNode(0)
curr = heada
for i in l:
    curr.next = ListNode(i)
    curr = curr.next

l = [2, 4]
headb = ListNode(3)
curr = headb
for i in l:
    curr.next = ListNode(i)
    curr = curr.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        while p != q:
            q = headB if q is None else q.next
            p = headA if p is None else p.next
        return p


s = Solution()
res = s.getIntersectionNode(heada, headb)
print(res)
