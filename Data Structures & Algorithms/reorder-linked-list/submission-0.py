# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split nodes in half using slow & fast
        # reverse the second half so we can add to the ans
        # add the two halves in in order

        # split nodes
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # set the second half
        second_half = slow.next
        # end the first half
        slow.next = None

        # reverse the second half
        prev_node = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev_node
            prev_node = second_half
            second_half = next_node

        # add in order
        first_half = head
        second_half = prev_node
        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = tmp1
            first_half, second_half = tmp1, tmp2
