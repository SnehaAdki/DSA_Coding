# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        temp = ListNode()
        original_head=  temp
        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val : 
                temp.next = ListNode(temp1.val)
                temp = temp.next
                temp1 = temp1.next
            else:
                temp.next = ListNode(temp2.val)
                temp = temp.next
                temp2 = temp2.next

        if temp1 is not None:
            temp.next = temp1
        if temp2 is not None:
            temp.next = temp2
        
        return original_head.next