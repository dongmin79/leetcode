from typing import Optional

from linkedlist import ListNode


class Solution:
    def get_len(self, node):
        node_len = 0
        while node:
            node = node.next
            node_len += 1
        return node_len

    def solution(self, head_a: Optional[ListNode], head_b: Optional[ListNode]):
        len_a, len_b = self.get_len(head_a), self.get_len(head_b)
        cur_a, cur_b = head_a, head_b
        if len_a > len_b:
            cur_a, cur_b = cur_b, cur_a
            len_a, len_b = len_b, len_a
        for _ in range(len_b - len_a):
            cur_b = cur_b.next
        while cur_a:
            if cur_a == cur_b:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None
