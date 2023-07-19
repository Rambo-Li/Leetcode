# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        for lst in lists:
            while lst:
                nums.append(lst.val)
                lst = lst.next
        
        nums = sorted(nums)

        res = curr = ListNode()
        for i in nums:
            curr.next = ListNode(i)
            curr = curr.next
        curr.next = None
        return res.next
    
# I think the recursive merging of two lists is the surposed answer. But this solution is fun because it dumps all the value and rebuild nodes with them, exploitation.