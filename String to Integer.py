class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strNoSpace = str.lstrip()
        if strNoSpace == '': return 0
        i = 0
        intger = 0
        signal = 1
        if strNoSpace[i] == '+':
        	signal = 1
        	i = i+1
        elif strNoSpace[i] == '-':
        	signal = -1
        	i = i+1
        while (i<len(strNoSpace)):
        	if (strNoSpace[i]<='9' and strNoSpace[i]>='0'):
        		intger = intger*10+int(strNoSpace[i])
        	else:
        		return intger*signal
        	MAX = 2**31 -1
        	MIN = -(2**31)
        	temp = signal*intger
        	if temp >=MAX: 
        		return MAX
        	elif temp <= MIN:
        		return MIN
        	i = i+1
        return intger*signal





