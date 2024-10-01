# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None

    def get_smallest(l1, l2):
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        return min(l1, l2, key=lambda x: x.val)

    head = get_smallest(list1, list2)
    if head == list1:
        list1 = list1.next
    else:
        list2 = list2.next
    cur = head
    while True:
        small = get_smallest(list1, list2)
        if small is None:
            return head
        if small == list1:
            cur.next = list1
            cur = cur.next
            list1 = list1.next
        else:
            cur.next = list2
            cur = cur.next
            list2 = list2.next
