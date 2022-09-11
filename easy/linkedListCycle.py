# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from operator import truediv
from typing import Optional


class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        current = head
        visited = set()

        while (current is not None):
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False

    # can also be solved with fast runner and slow runner
        
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while (fast is not None):
            if(fast.next is None):
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False