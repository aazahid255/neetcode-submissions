# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# input: head of linekd list, integer n to remove from linked list
# output: list with head removed
# edge cases: empty list, only one node inlist

# fast and slow pionter?
# dummy node?

# why dont i just iterate n times to before where i need to remove it and then do curr.next/next?


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
            
