from linkedlist import ListNode


class Solution:
    def remove(self, head: ListNode, n: int):
        dummy_head = ListNode(0, head)
        slow = dummy_head
        fast = dummy_head
        for i in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = not slow.next.next
        return dummy_head.next
