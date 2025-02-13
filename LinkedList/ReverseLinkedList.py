
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        curr = head
        prev = None
        nex = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev