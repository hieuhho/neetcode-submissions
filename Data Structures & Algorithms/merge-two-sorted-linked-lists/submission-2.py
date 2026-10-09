# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # set up a node
        head = current = ListNode()

        # add the smaller val to current.next
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # move forward
            current = current.next
        
        # if a list if empty, add the rest of the other to end
        current.next = list1 or list2
        
        # return the node (.next since default is 0)
        return head.next
