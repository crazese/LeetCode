# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        cur = l3
        sum = 0
        while 1:
            if l1 !=None:
                sum = sum+l1.val
                l1 = l1.next
            if l2 !=None:
                sum = sum+l2.val
                l2 = l2.next
            num = sum%10
            sum = sum/10
            cur.val = num
            if l1!=None or l2!=None or sum!=0:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                break
        return l3
            