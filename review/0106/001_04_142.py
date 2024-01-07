from typing import Optional

from linkedlist import ListNode


class Solution:
    def solution(self, head: Optional[ListNode]):
        # 12345674
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next  # 2
            fast = fast.next.next  # 3

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
