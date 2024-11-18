from src.reverse_linked_list import ListNode, reverse_linked_list


def list_to_linked_list(elements: list[int]) -> ListNode | None:
    if not elements:
        return None

    head = ListNode(elements[0])
    current = head

    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next

    return head


def linked_list_to_list(head: ListNode) -> list:
    elements = []

    while head:
        elements.append(head.val)
        head = head.next

    return elements


def test_reverse_empty_list() -> None:
    head = list_to_linked_list([])
    reversed_head = reverse_linked_list(head)

    assert linked_list_to_list(reversed_head) == []


def test_reverse_single_node() -> None:
    head = list_to_linked_list([1])
    reversed_head = reverse_linked_list(head)

    assert linked_list_to_list(reversed_head) == [1]


def test_reverse_multiple_nodes() -> None:
    head = list_to_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)

    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]


def test_reverse_two_nodes() -> None:
    head = list_to_linked_list([1, 2])
    reversed_head = reverse_linked_list(head)

    assert linked_list_to_list(reversed_head) == [2, 1]


def test_reverse_large_list() -> None:
    head = list_to_linked_list(list(range(1000)))
    reversed_head = reverse_linked_list(head)

    assert linked_list_to_list(reversed_head) == list(range(999, -1, -1))
