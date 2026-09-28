# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        curr = head
        while curr:
            total +=1 
            curr = curr.next
        
        nth = total - n

        if nth == 0:
            head = head.next
            return head

        dummy = head
        prev = None
        for i in range(nth):
            prev = dummy
            dummy = dummy.next

        prev.next = dummy.next
        dummy.next = None

        return head
        
        