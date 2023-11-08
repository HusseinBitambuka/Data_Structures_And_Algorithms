def reverseLinkedList(head):
    reversedList = None
    if not head.next:
        return head
    else:
        reversedList = reverseLinkedList(head.next)
        head.next.next = head
        head.next = None