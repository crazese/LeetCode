# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        if l == 0:
            return []
        if l ==1:
            return lists[0]

        left = self.mergeKLists(lists[:l/2])
        right = self.mergeKLists(lists[l/2:])

        res = ListNode(0)
        cur = res

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right
        return res.next