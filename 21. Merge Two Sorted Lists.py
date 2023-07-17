class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            if curr1.val <= curr2.val:
                if temp1 == None or temp1.val > curr2.val:
                    curr1.next = curr2
                curr1 = temp1
            else:
                if temp2 == None or temp2.val >= curr1.val:
                    curr2.next = curr1
                curr2 = temp2
                
        return list1 if list1.val <= list2.val else list2
    

# This is a surprisingly complicated problem because the two list have different in-place merging behavior. The active list(merge when equal) needs to link 
# its next node when the other node and its next node are equal, while the passive list(not merge when equal) needs to link the active list node when its
# next node and the other list node are equal. Only doing this, you can form a completely merged list.