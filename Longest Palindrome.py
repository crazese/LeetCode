class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        sum = 0
        flag = 0
        for i in s:
            count[i] = count[i]+1 if i in count else 1
        
        for i in count.values():
            if i%2 == 0:
               sum = sum+i
            else:
                sum = sum+i-1
                flag = 1
        if flag:
            sum = sum+1
        return sum