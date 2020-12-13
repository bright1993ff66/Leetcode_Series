# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_141:
    def hasCycle_141_1(self, head: ListNode) -> bool:
        dictionary = {}
        while head:
            if head in dictionary:
                return True
            else:
                dictionary[head]= True
            head = head.next
        return False

    def hasCycle_141_2(self, head: ListNode) -> bool:
        if not head or not head.next: return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class Solution_142:
    def detectCycle_142_1(self, head: ListNode) -> ListNode:
        dictionary = {}
        index_val = 0
        while head:
            if head in dictionary:
                return head
            else:
                dictionary[head] = index_val
            head = head.next
            index_val += 1
        return None

    def detectCycle_142_2(self, head: ListNode) -> ListNode:
        if not head or not head.next: return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return slow
