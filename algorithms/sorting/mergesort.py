class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def mergeTwoList(l1, l2):
    head = Node()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return head.next

def mergesort(head):
    if not head or not head.next:
        return head
    
    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None

    left = mergesort(head)
    right = mergesort(after_middle)

    return mergeTwoList(left, right)


n1 = Node(5, Node(7, Node(2, Node(3, Node(1, Node(6, Node(4)))))))
n2 = mergesort(n1)
print(n2)
    