# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currentnode = head
        totalLength = 0 
        while(currentnode): 
            totalLength += 1 
            currentnode = currentnode.next 
        removeIndex = totalLength - n

        currentnode = head
        
        if removeIndex == 0:
            return head.next
        remindex = 0 

        while(currentnode): 
            if (remindex == removeIndex - 1):
                break 
            currentnode = currentnode.next 
            remindex+=1
        if currentnode and currentnode.next: 

            currentnode.next = currentnode.next.next 
        

        return head 




        