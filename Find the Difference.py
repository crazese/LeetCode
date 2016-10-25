class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = s+t
        letters = {}
        for i in l:
            letters[i] = letters[i]+1 if i in letters else 1
        for k,v in letters.iteritems():
            if v%2 ==1:
                return k



sol = Solution()
print sol.findTheDifference('abcc','eabcc')