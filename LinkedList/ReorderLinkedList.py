# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return head
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        first, second = head, prev

        while second:
            dummy1 = first.next
            dummy2 = second.next

            first.next = second
            second.next = dummy1

            first = dummy1
            second = dummy2
        

            
