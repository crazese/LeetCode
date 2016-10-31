# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return root.left.val+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
            if root.left:
                return root.left.val+self.sumOfLeftLeaves(root.left)
            if root.right:
                return self.sumOfLeftLeaves(root.right)

        return 0