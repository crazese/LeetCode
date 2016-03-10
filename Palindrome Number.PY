class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x ==0: return True
        MAX = 2**31 -1
        MIN = -2**31
        if x>MAX: x = MAX
        if x<MIN: x = MIN
        temp = x
        sum = 0
        while (temp>0):
            num = temp%10
            sum = sum*10 + num
            temp = temp/10
        
        if sum == x:
            return True
        else:
            return False
            
        