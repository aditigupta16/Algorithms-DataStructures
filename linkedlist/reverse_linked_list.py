# Reverse a linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    if not head or not head.next:
        return head

    reversed_list = reverse_list(head.next) 

    if not head.next.next:
        head.next.next = head
        head.next = None

    return reversed_list
        
def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next


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
    reversed_list = reverse_list(node_1)
    print_linked_list(reversed_list)
