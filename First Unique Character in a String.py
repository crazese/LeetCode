class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for i in s:
            index = ord(i)-ord('a')
            count[i] = count[i]+1 if i in count else 1
        
        for i in xrange(len(s)):
            if count[s[i]] == 1:
                return i
        return -1