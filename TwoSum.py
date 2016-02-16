class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pre = 0
        for idx in nums:
        	fid = target - idx
         	if fid in nums:
         	    bre = nums.index(fid)
         	    if bre !=pre:
        		    return [pre,bre]
        	pre = pre+1