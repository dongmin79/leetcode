from linkedlist import ListNode


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def reverse_list1(self, head: ListNode) -> ListNode:
        return self.helper(head, None)

    def helper(self, cur: ListNode, pre: ListNode) -> ListNode:
        if cur == None:
            return pre
        temp = cur.next
        cur.next = pre
        return self.helper(temp, cur)
