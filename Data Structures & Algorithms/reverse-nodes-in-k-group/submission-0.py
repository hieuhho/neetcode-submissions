# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_K_val(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            previous, current = kth.next, group_prev.next
            while current != group_next:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp

            group_tmp = group_prev.next
            group_prev.next = kth
            group_prev = group_tmp
        return dummy.next

    def get_K_val(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current