# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode()
        start.next = head
        prev_group_end = start
        kn = group_head = head
        while True:
            for i in range(k-1):
                if not kn:
                    break
                kn = kn.next
            temp = kn.next if kn else None
            
            if kn:
                temp1 = group_head
                left, right = group_head, kn
                while left != kn:
                    nex = left.next
                    left.next = kn.next
                    kn.next = left
                    left = nex
                prev_group_end.next = kn
                prev_group_end = temp1
                kn = group_head = temp
            else:
                break
        return start.next