from typing import Optional

from linkedlist import ListNode


class Solution:
    def solution(self, head: Optional[ListNode], n):
        dummy_head = ListNode(0, head)
        slow = fast = dummy_head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy_head.next
