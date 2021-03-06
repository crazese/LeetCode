# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = ListNode(0)
        l.next = head
        p,q = l,l
        while n>0:
            n = n-1
            q = q.next

        while q.next is not None:
            q = q.next
            p = p.next

        temp = p.next
        p.next = temp.next

        return l.next
