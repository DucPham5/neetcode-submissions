# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen = {}

        curr = head 
        index = 0
        while curr:
            seen[index] = curr
            curr = curr.next
            index+=1

        
        for i in range(index):
            node1 = seen[i]#0
            node2 = seen[index-i-1]#n-1
            if node1 == node2:
                node1.next = None
                break
            after = node1.next
            node1.next = node2
            if node2 == after:
                node2.next = None
                break
            else:
                node2.next = after
        


        