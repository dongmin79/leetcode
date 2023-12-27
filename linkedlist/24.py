from typing import Optional

from linkedlist import ListNode


class Solution:
    def swap_paris(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pre = head
        cur = head.next
        next = head.next.next

        cur.next = pre
        pre.next = self.swap_paris(next)
        return cur

    def swap_paris2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next and current.next.next:
            temp = current.next  # 防止节点修改
            temp1 = current.next.next.next

            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        return dummy_head.next
