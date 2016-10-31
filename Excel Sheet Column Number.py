class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in xrange(len(s)):
            num = num+26**(len(s)-1-i)*(ord(s[i])-ord('A')+1)
        return num
        