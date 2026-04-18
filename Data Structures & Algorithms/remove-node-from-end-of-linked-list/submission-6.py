# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head

        curr = temp
        i = 0
        sremove = temp
        
        while curr.next:
            if i >= n:
                sremove = sremove.next
            i+=1
            curr = curr.next
        
        sremove.next = sremove.next.next



        return temp.next






