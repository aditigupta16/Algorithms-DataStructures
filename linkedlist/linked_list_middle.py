# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head):
    if not head:
        return
    fast_ptr = head
    slow_ptr = head

    while fast_ptr.next and fast_ptr.next.next:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    if fast_ptr.next:
        slow_ptr = slow_ptr.next

    print(slow_ptr.val)


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    middle_node(node_1)