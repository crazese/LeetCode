class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isBrackets = []
        l = len(s)
        for i in xrange(l):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                isBrackets.append(s[i])

            if s[i]==')':
                if len(isBrackets) == 0:
                    return False
                elif isBrackets[-1]=='(':
                    isBrackets=isBrackets[:-1]
                else:
                    isBrackets.append(s[i])

            if s[i]==']':
                if len(isBrackets) == 0:
                    return False
                elif isBrackets[-1]=='[':
                    isBrackets = isBrackets[:-1]
                else:
                    isBrackets.append(s[i])

            if s[i]=='}':
                if len(isBrackets) == 0:
                    return False
                elif isBrackets[-1] == '{':
                    isBrackets = isBrackets[:-1]
                else:
                    isBrackets.append(s[i])



        if len(isBrackets)>0:
            return False
        else:
            return True

