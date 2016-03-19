class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 1000-M, 500-D, 100-C, 50-L, 10-X, 5-V, 1-I
        roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        temp = num
        i = 0
        res = ''
        while (temp>0):
        	if temp >=val[i]:
        		temp = temp - val[i]
        		res = res+roman[i]
        	else:
        		i = i+1
        return res


test = Solution()
print test.intToRoman(2)