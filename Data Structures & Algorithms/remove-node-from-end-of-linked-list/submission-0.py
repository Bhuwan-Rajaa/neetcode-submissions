# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i = 0
        if n == 1:
            head = None
            return head
            
        while i != n-1 and curr:
            curr = curr.next
            i+=1

        if curr.next == None:
            curr = None
            return head

        curr.next = curr.next.next
        return head
        