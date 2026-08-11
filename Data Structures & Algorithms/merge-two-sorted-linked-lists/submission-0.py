# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        while list1 and list2: 

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next # Advance list 1
            else: 
                tail.next = list2
                list2 = list2.next# Advance list 2
            tail = tail.next # Advance the tail
        tail.next = list1 if list1 else list2 #attach leftover
        return dummy.next 
                

        
        