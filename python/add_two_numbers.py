from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_string: str = ""
    l3_string: str = ""
    p1 = l1
    while p1.next is None:
        l1_string += p1.val
        p1 = p1.next

    print(l1_string)


def main():
    pass


if __name__ == "__main__":
    main()
