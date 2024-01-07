from linkedlist import ListNode


class Solution:
    def solution(self, head: ListNode):
        dummy_head = ListNode(next=head)
        current = dummy_head
        #  1234
        #  2134
        while current.next and current.next.next:
            temp = current.next  # 1
            temp1 = current.next.next.next  # 3

            current.next = current.next.next  # 头节点->2
            current.next.next = temp  # 2节点->1节点
            temp.next = temp1
            current = current.next.next
        return dummy_head.next

    def solution1(self, head: ListNode):
        #  1234
        #  2134
        if head is None or head.next is None:
            return head
        pre = head  # 1
        cur = head.next  # 2
        next = head.next.next  # 3
        cur.next = pre # 2-1
        pre.next = self.solution1(next)
        return cur
