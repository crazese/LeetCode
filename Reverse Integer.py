class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0 or abs(x)>=2**32:return 0
        sym = x/abs(x)
        x= abs(x)
        y = 0
        while x >= 1:
        	y = y*10 + x%10
        	x = x/10
        if y>=2**32: return 0
        y = y*sym
        return y


# test = Solution()
# print test.reverse(1534236469)

