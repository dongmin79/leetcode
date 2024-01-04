from typing import Optional

from linkedlist import ListNode


class Solution:
    def helper(self, cur, pre):
        if cur is None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.helper(temp, cur)

    def solution(self, head=Optional[ListNode]):
        # 1-2-3-4-5-null
        #  5-4-3-2-1-null
        self.helper(head, None)

    def solution1(self, head: ListNode):
        cur = head
        pre = None
        # pre 0 cur 1 cur.next 2
        # pre 1 cur 2 cur.next 0
        # pre=cur cur= cur.next cur.next=pre
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
