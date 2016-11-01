class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            count[i] = count[i]+1 if i in count else 1
        for k,v in count.iteritems():
            if v>int(len(nums)/2):
                return k
        
                
        