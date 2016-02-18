class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxL = 0
        first = 0
        cur = 0
        recent = {}
        """
        find the first repeating charator, thus first-i is the solution
        """
        for k,v in enumerate(s):
            if v in recent and recent[v]>=first:
                first = recent[v]+1
            recent[v] = k
            maxL =  max(maxL, k+1-first)
        return maxL
            
  