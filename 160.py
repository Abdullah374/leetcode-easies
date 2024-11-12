from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersectVal = 0
        first = headA
        second = headB
        while first != second:
            first = first.next if first else headB
            second = second.next if second else headA
        
        return first

        

        

            

