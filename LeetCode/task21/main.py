# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        elem_list1 = list1
        elem_list2 = list2
        answer = ListNode()
        elem_answer = answer
        while elem_list1 is not None and elem_list2 is not None:
            if elem_list1.val < elem_list2.val:
                elem_answer.next = elem_list1
                elem_answer = elem_answer.next
                elem_list1 = elem_list1.next
            else:
                elem_answer.next = elem_list2
                elem_answer = elem_answer.next
                elem_list2 = elem_list2.next
        while elem_list1 is not None:
            elem_answer.next = elem_list1
            elem_answer = elem_answer.next
            elem_list1 = elem_list1.next
        while elem_list2 is not None:
            elem_answer.next = elem_list2
            elem_answer = elem_answer.next
            elem_list2 = elem_list2.next
        return answer.next
