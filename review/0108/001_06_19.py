from typing import Optional

from linkedlist import ListNode


class Solution:
    def solution(self, head: Optional[ListNode], n: int):
        # 12345
        # 1235
        dummy_head = ListNode(next=head)
        slow = fast = dummy_head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_head.next
