from typing import Optional, Union


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Union['Node', None] = None

    @staticmethod
    def create_linked_list(arr: list[int]) -> Optional['Node']:
        if not arr:
            return None
        head = Node(arr[0])
        current = head
        for i in range(1, len(arr)):
            current.next = Node(arr[i])
            current = current.next
        return head
    
    @staticmethod
    def print_linked_list(head: Optional['Node']) -> None:
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()


asserstion = {
    1: ([1, 2, 3], [3, 2, 1]),
    2: ([1], [1]),
    3: ([], []),
    4: ([1, 2, 3, 4], [4, 3, 2, 1])
}

def reverse_linked_list(head: Optional['Node']) -> Optional[Node]:
    if not head:
        return None
    
    rev: Optional[Node]= None

    while head:
        rev, rev.next, head = head, rev, head.next
    return rev

for k, v in asserstion.items():
    reversed = reverse_linked_list(Node.create_linked_list(v[0]))

    if reversed is None:
        continue

    else:
        for num in v[1]:
            assert reversed.data == num
            reversed = reversed.next
    
print("passed")


