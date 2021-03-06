# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = None
        head = None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                if node is None:
                    node = l1
                    head = node
                else:
                    node.next = l1
                    node  = node.next
                l1 = l1.next

            else:
                if node is None:
                    node = l2
                    head = node
                else:
                    node.next = l2
                    node = node.next
                l2 = l2.next

        if l1 is not None:
            node.next = l1

        if l2 is not None:
            node.next = l2

        return head