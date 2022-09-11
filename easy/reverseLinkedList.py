# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head

        head, tail = self.reverse(head)
        tail.next = None
        return head

    def reverse(self, head):
        if head.next is None:
            return head, head
        else:
            start, end = self.reverse(head.next)
            end.next = head
            return start, head

# can be do iteratively without stack, just need 3 pointers