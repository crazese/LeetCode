class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}
        inter = []
        for i in nums1:
            count[i] = 1
            
        for i in nums2:
            if i in count and i not in inter:
                inter.append(i)
        return inter
                