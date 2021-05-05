# 给你一个链表数组，每个链表都已经按升序排列。
#
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
#  示例 1：
#
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
#  示例 2：
#
#  输入：lists = []
# 输出：[]
#
#
#  示例 3：
#
#  输入：lists = [[]]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  k == lists.length
#  0 <= k <= 10^4
#  0 <= lists[i].length <= 500
#  -10^4 <= lists[i][j] <= 10^4
#  lists[i] 按 升序 排列
#  lists[i].length 的总和不超过 10^4
#
#  Related Topics 堆 链表 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     '我的答案：执行耗时:7156 ms,击败了5.00% 的Python3用户；内存消耗:409.2 MB,击败了5.01% 的Python3用户'
# def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#     def helper(l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1 and not l2:
#             return
#
#         node = ListNode(None)
#         res = node
#         # node.next = l1
#         # node = node.next  # todo
#         # res = node
#
#         while l1 or l2:
#             if l1 and l2:
#                 if l1.val <= l2.val:  # todo 我仅仅是把 node.next = ListNode(l1.val)改成了 node.next = l1
#                     node.next = l1
#                     l1 = l1.next
#                 elif l1.val > l2.val:
#                     node.next = l2
#                     l2 = l2.next
#                 node = node.next
#
#             elif l1:
#                 node.next = l1
#                 break
#             elif l2:
#                 node.next = l2
#                 break
#
#         return res.next
#
#     if len(lists)==0:
#         return
#     elif len(lists)==1:
#         return lists[0]
#     elif len(lists)==2:
#         return helper(lists[0],lists[1])
#     else:
#         return self.mergeKLists([helper(lists[0],lists[1])]+lists[2:])

# def mergeKLists(self, lists):
#     q = []
#     for i, head in enumerate(lists):
#         if head:
#             heappush(q, (head.val, i, head))
#
#     node = dummy = ListNode(0)
#     while q:
#         val, i, pop_node = heappop(q)
#         print(val)
#         node.next = ListNode(val)
#         node = node.next
#         next_node = pop_node.next
#         if next_node:
#             heappush(q, (next_node.val, i, next_node))
#     return dummy.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        temp = ListNode(None)
        res = temp

        while heap:
            # temp.next = ListNode(heap.pop())
            temp.next = ListNode(heapq.heappop(heap))
            temp = temp.next
        return res.next

        # heap = []
        # for node in lists:
        #     while node:
        #         heapq.heappush(heap, node.val)
        #         node = node.next
        #
        # temp = ListNode(-1)
        # head = temp
        # while heap:
        #     smallestNode_val = heapq.heappop(heap)
        #     temp.next = ListNode(smallestNode_val)
        #     temp = temp.next
        #
        # return head.next

# leetcode submit region end(Prohibit modification and deletion)
