# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        
        curr = None

        if list1.val <= list2.val:
            curr = list1
            nextHead = self.mergeTwoLists(list1.next, list2)
            curr.next = nextHead
        else:
            curr = list2
            nextHead = self.mergeTwoLists(list1, list2.next)
            curr.next = nextHead
        
        return curr