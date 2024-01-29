from typing import Optional

from linkedlist import ListNode


class Solution:
    def solution(self, head: Optional[ListNode]):
        # cur-1-2-3-4
        dummy_head = ListNode(next=head)
        current = dummy_head
        while current.next and current.next.next:
            # 1
            temp = current.next
            # 3
            temp1 = current.next.next.next
            # cu1-2
            current.next = current.next.next
            # 2-1
            current.next.next = temp
            # 1-3
            temp.next = temp1
            # 2
            current = current.next.next
