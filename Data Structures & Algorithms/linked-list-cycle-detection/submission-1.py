# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fcurr = scurr = head
        
        while fcurr and fcurr.next:
            fcurr = fcurr.next.next
            scurr = scurr.next
            if fcurr == scurr:
                return True
        return False