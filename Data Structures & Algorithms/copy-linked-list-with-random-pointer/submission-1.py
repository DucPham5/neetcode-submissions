"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}
        curr = head
        if head is None:
            return None

        while curr:
            copy = Node(curr.val)
            seen[curr] = copy
            curr = curr.next
        
        curr = head

        while curr:
            copy = seen[curr]
            copy.next = seen[curr.next] if curr.next else None
            copy.random = seen[curr.random] if curr.random else None
            curr = curr.next
            

        return seen[head]

        