# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                duplicate_value = current.val
                while current and current.val == duplicate_value:
                    current = current.next
                previous.next = current
            else:
                previous = current
                current = current.next

        return dummy.next
