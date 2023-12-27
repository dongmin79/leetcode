from linkedlist import ListNode


class Solution:
    def method1(self, head_a: ListNode, head_b: ListNode):
        len_a, len_b = 0, 0
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
            if cur_a == cur_b:
                return cur_a
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
        return None