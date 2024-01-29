from typing import Optional

from linkedlist import ListNode


class Solution:
    def solution(self, head_a: Optional[ListNode], head_b: Optional[ListNode]):
        len_a = 0
        len_b = 0
        cur = head_a
        while cur:
            cur = cur.next
            len_a += 1
        cur = head_b
        while cur:
            cur = cur.next
            len_b += 1
        cur_a, cur_b = head_a, head_b
        if len_a > len_b:
            cur_a, cur_b = cur_b, cur_a
            len_a, len_b = len_b, len_a
        for _ in range(len_b - len_a):
            cur_b = cur_b.next
        while cur_a:
            if cur_b == cur_a:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None
