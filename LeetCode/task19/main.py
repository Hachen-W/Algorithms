# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        node_temp = head
        while node_temp is not None:
            list_length += 1
            node_temp = node_temp.next
        if n == list_length:
            head = head.next
        else:
            node_temp = head
            for index in range(list_length - n - 1):
                node_temp = node_temp.next
            node_temp.next = node_temp.next.next
        return head
