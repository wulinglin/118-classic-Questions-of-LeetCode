# 给定一个链表，判断链表中是否有环。
#
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的
# 位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
#  如果链表中存在环，则返回 true 。 否则，返回 false 。
#
#
#
#  进阶：
#
#  你能用 O(1)（即，常量）内存解决此问题吗？
#
#
#
#  示例 1：
#
#
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#  示例 2：
#
#
#
#  输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#  示例 3：
#
#
#
#  输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
#  提示：
#
#
#  链表中节点的数目范围是 [0, 104]
#  -105 <= Node.val <= 105
#  pos 为 -1 或者链表中的一个 有效索引 。
#
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"方法一：哈希表：o(N)内存"


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        head_set = set()
        while head:
            if head in head_set:  # todo 这里不是head.val哈，有可能重复。
                return True
            head_set.add(head)
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


# 判断环的入口点：

"""判断有环：
slow每次向前走一步，fast向前追了两步，因此每一步操作后fast到slow的距离缩短了1步，这样继续下去就会使得
两者之间的距离逐渐缩小：...、5、4、3、2、1、0 -> 相遇。又因为在同一个环中fast和slow之间的距离不会大于换的长度，因此
到二者相遇的时候slow一定还没有走完一周（或者正好走完以后，这种情况出现在开始的时候fast和slow都在环的入口处）。

#      https://www.cnblogs.com/yorkyang/p/10876604.html
# 可以看出，从链表起点head开始到入口点的距离a,与从slow和fast的相遇点（如图）到入口点的距离相等。
# 因此我们就可以分别用一个指针（ptr1, prt2），同时从head与slow和fast的相遇点出发，每一次操作走一步，直到ptr1 == ptr2，此时的位置也就是入口点！

"""


# @param head ListNode类
# @return ListNode类
# #
# class Solution:
#     def detectCycle(self , head ):
#         # write code here
#         a = []
#         while head:
#             if head in a:
#                 return head
#             else:
#                 a.append(head)
#             head=head.next
#         return

# write code here


class Solution:
    def detectCycle(self, head):
        # 首先判断是否存在环
        fastHead = head
        slowHead = head

        while (fastHead and fastHead.next):
            fastHead = fastHead.next.next
            slowHead = slowHead.next
            if fastHead == slowHead:
                break
        # 本想用快慢指针是否相等作为判断条件，但初始时快慢指针是相等的
        if fastHead == None or fastHead.next == None:
            return None
        fastHead = head
        while (fastHead != slowHead):
            fastHead = fastHead.next
            slowHead = slowHead.next
        return fastHead

# leetcode submit region end(Prohibit modification and deletion)
