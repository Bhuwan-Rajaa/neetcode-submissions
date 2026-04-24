# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i = 0
        re = head
        if n ==1:
            head = None
            return head
        while curr.next:
            if i >= n:
                re = re.next
            i+=1
            curr = curr.next

        if re == head: 
            head = head.next
        else: re.next = re.next.next
        return head