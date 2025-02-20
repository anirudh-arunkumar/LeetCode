
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        if not head:
            return head
        
        curr = head
        copy = {}
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            copy[curr].next = copy.get(curr.next)
            copy[curr].random = copy.get(curr.random)
            curr = curr.next
        
        return copy[head]
            


            