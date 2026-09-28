# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node2 = slow.next
        prev = slow.next = None
        while node2:
            after = node2.next
            node2.next = prev
            prev = node2
            node2 = after
    
        node2 = prev
        node1 = head
        while node2:
            tmp1,tmp2 = node1.next, node2.next
            node1.next = node2
            node2.next = tmp1
            node1,node2 = tmp1,tmp2


        