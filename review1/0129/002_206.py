from typing import Optional

from linkedlist import ListNode


class Solution:
    def solution(self, head: Optional[ListNode]):
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
