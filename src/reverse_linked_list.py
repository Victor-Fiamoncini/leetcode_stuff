"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    # Two pointers approach
    current = head
    previous = None

    while current:
        temp = current.next

        current.next = previous

        previous = current

        current = temp

    return previous
