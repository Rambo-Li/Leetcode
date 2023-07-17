# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        curr = head
        while curr:
            q.append(curr)
            curr = curr.next
        while q:
            left = q.popleft()
            right = q.pop() if q else None
            temp = left.next
            left.next = right
            if right:
                right.next = temp if right != temp else None

# I use a double-end-queue then pop from both ends. The majority sulutions use slow and fast pointers to get the mid then reverse the second half then merge, truely in-place.