# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root:
            leftMaxDepth = self.maxDepth(root.left)
            rightMaxDepth = self.maxDepth(root.right)
            sonMaxDepth = max(leftMaxDepth,rightMaxDepth)
            depth = depth + sonMaxDepth
        depth = depth+1
        return depth