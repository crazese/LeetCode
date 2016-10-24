class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rlist = []
        for i in xrange(1,n+1):
            print i
            if i%3==0 and i%4==0:
                rlist.append("FizzBuzz")
            elif i%3==0:
                rlist.append("Fizz")
            elif i%4==0:
                rlist.append("Buzz")
            else:
                rlist.append(str(i))
        return rlist

sol = Solution()
print sol.fizzBuzz(5)
