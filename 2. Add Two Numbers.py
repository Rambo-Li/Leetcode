# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        start = head = ListNode()
        prev = None
        while curr1 or curr2:
            if curr1 and curr2:
                carry, remainder = divmod((curr1.val + curr2.val + head.val), 10)
            elif curr1:
                carry, remainder = divmod((curr1.val + head.val), 10)
            else:
                carry, remainder = divmod((curr2.val + head.val), 10)

            head.val = remainder 
            head.next = ListNode(carry)
            prev = head
            head = head.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        if head.val == 0:
            prev.next = None
        return start
    
# A sincct way is to include the carry in the while loop so don't need to write the last if condition.