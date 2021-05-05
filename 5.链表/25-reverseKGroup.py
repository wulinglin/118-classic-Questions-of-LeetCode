"""每K个- -组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5


说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ./

    reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    """1.初始固定pred phead cur tail
    2.pre.next=cur.next
    3.cur.next=tail.next
    4.tail.next = cut
    5.重置pre phead cur tail
    6.return phead.next
    """


# 方法一：stack ， stack的先进后出方式具有天然的翻转属性
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr_idx = 0
        if not head:
            return head

        stack = []
        curr = head
        while curr:
            curr_idx += 1
            stack.append(curr.val)
            if curr_idx % k == 0:
                if curr_idx // k == 1:  # 重重重要！
                    new_head = ListNode(stack.pop())  # todo 有没有更优雅的写法
                    new_curr = new_head
                while stack:
                    new_curr.next = ListNode(stack.pop())
                    new_curr = new_curr.next
            curr = curr.next

        if curr_idx < k:  # todo 有没有更优雅的写法
            new_head = ListNode(stack[0])
            stack.remove(stack[0])
            new_curr = new_head
        while len(stack) > 0:
            new_curr.next = ListNode(stack[0])
            stack.remove(stack[0])
            new_curr = new_curr.next
        return new_head


# # 方法二：链表翻转：头插法&尾插法
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        phead = ListNode(None)
        phead.next, pre, tail = head, phead, phead  # tail = phead ?
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = pre.next  # todo 为啥这里
            while pre.next != tail:  # 链表是可以有重复的值的。这种等于的写法，是指指针指向的内存地址相同
                #  12345  23145 pre-cur-tail!
                # 得到下一个元素
                cur = pre.next
                # pre与cur.next 连接起来，画图可以看出来
                # cur是新的链表的第一个节点
                pre.next = cur.next
                cur.next = tail.next
                # 每次第一个节点都要知道插谁后面，这一句就是为了更新
                tail.next = cur
            # 当前面都已经反转完毕，就要进行要一个k组的转换，需要更新，pre和tail
            # 按照k=3的例子，此时pre和tail就指向1这个节点，而我们第一步创建的pre和tail
            # 指向的是我们自己建立的节点 感受一下建立一个新的头节点的好处
            # todo 为啥这里等于head是指向1
            pre = head
            tail = head
        return phead.next


# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
#         pre = dummy
#         tail = dummy
#         while True:
#             count = k
#             while count and tail:
#                 count -= 1
#                 tail = tail.next
#             if not tail: break
#             head = pre.next
#             while pre.next != tail:
#                 cur = pre.next # 获取下一个元素
#                 # pre与cur.next连接起来,此时cur(孤单)掉了出来
#                 pre.next = cur.next
#                 cur.next = tail.next # 和剩余的链表连接起来
#                 tail.next = cur #插在tail后面
#             # 改变 pre tail 的值
#             pre = head
#             tail = head
#         return dummy.next


# # 方法三：递归
#
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         if not head or not head.next:
#             return head
#
#         curr = head
#
#         count = 0
#         while curr and count != k:
#             count += 1
#             curr = curr.next
#
#         if count == k:
#             self.reverseKGroup(curr, k)
#             while count > 0:
#                 temp = head.next
#                 head.next = curr
#                 curr = head
#                 head = temp
#
#                 # temp = head.next
#                 # head.next = curr
#                 # curr = head
#                 # head = temp
#                 count -= 1
#             head = curr
#         return head
#     #        Node = None
#     #        while head:
#     #             p = head
#     #             head = head.next
#     #             p.next = Node
#     #             Node = p


k = 2
k = 3
l = [2, 3, 4, 5]
# l = [5]
head = ListNode(1)
curr = head
for i in l:
    curr.next = ListNode(i)
    curr = curr.next

s = Solution()
new_head = s.reverseKGroup(head, k)
while new_head:
    print(new_head.val)
    new_head = new_head.next

# class Solution:
#     # 返回ListNode
#     def ReverseList(self, p_head):
#         # write code here
#         if p_head == None or p_head.next == None:
#             return p_head
#         cur = p_head
#         tmp = None
#         newhead = None
#         while cur:
#             tmp=cur.next
#             cur.next=newhead
#             newhead=cur # TODO 顺序不对都会错
#             cur=tmp
#         return newhead

# 以下是链表翻转的代码：https://blog.csdn.net/weixin_39561100/article/details/79818949
# class Solution:
#     # 返回ListNode
#     def ReverseList(self, p_head):
#         # write code here
#         if p_head == None or p_head.next == None:
#             return p_head
#         cur = p_head
#         tmp = None
#         newhead = None
#         while cur:
#             tmp = cur.next
#             cur.next = newhead
#             newhead = cur  # todo why
#             cur = tmp
#         return newhead


"""测试"""


# head = ListNode(1)
# curr = head
# for i in [2, 3, 4, 5]:
#     curr.next = ListNode(i)
#     curr = curr.next
# s = Solution()
# new_head = s.ReverseList(head)
# print(new_head)
# while new_head:
#     print(new_head.val)
#     new_head = new_head.next


#  可以修改原链表的话，更简单
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        Node = None
        while head:
            p = head
            head = head.next
            p.next = Node
            Node = p
        return Node


# 递归的方法
class Solution:
    # 返回ListNode
    def ReverseList(self, p_head):
        # write code here
        if not p_head or not p_head.next:
            return p_head
        new_head = self.ReverseList(p_head.next)
        p_head.next.next = p_head
        p_head.next = None
        return new_head
