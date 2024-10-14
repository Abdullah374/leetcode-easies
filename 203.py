from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if head is None:
#             return head
        

        
#         # while head:
#         #     if head.val == val:
#         #         head = head.next
#         #     if head.next and head.next.val == val:
#         #         head.next = head.next.next
#         #     if head.next and head.next.next is None and head.next.val == val:
#         #         head.next = None
#         #     head = head.next
       
            
#         slow = head

#         while slow:
#             if head.val ==val:
#                 head = head.next
#                 slow = head
#                 continue
            
#             if slow.next and slow.next.val == val:
#                 slow.next = slow.next.next
#             elif slow.next and slow.next.next is None and slow.next.val == val:
#                 slow.next = None
#             slow = slow.next
            

#         return head
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy

        while slow and slow.next:
            if slow.next.val == val:
                slow.next = slow.next.next
            else:
                slow = slow.next
        return dummy.next
