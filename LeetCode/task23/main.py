# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = None
        array = []
        for list_cur in lists:
            while list_cur is not None:
                array.append(list_cur.val)
                list_cur = list_cur.next
        array.sort()
        node_cur = None
        for elem in array:
            if node_cur is None:
                node_cur = ListNode()
                answer = node_cur
            else:
                node_cur.next = ListNode()
                node_cur = node_cur.next
            node_cur.val = elem
        return answer
