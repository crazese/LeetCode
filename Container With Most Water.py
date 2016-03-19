class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxc = 0
        while left < right:
        	temp = min([heightleft],height[right])*(right - left)
        	if temp >maxc:
        		maxc = temp

        	if height(left)>height(right):
        		right = right - 1
        	else:
        		left = left +1

       	return maxc

