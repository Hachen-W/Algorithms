from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getValue(self, listNode: Optional[ListNode]) -> int:
        result = 0
        degree = 0
        while listNode is not None:
            result += listNode.val * 10 ** degree
            listNode = listNode.next
            degree += 1
        return result

    def valueToListNode(self, value: int) -> Optional[ListNode]:
        head = ListNode(value % 10)
        temp = head
        value //= 10
        while value > 0:
            temp.next = ListNode(value % 10)
            temp = temp.next
            value //= 10
        return head

    def addTwoNumbers(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
            ) -> Optional[ListNode]:
        first_number = self.getValue(l1)
        second_number = self.getValue(l2)
        return self.valueToListNode(first_number + second_number)
