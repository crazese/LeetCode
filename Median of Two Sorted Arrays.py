class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1)+len(nums2)
        if total%2==0:
            return float(self.findMedian(nums1,len(nums1),nums2,len(nums2),total/2)+self.findMedian(nums1,len(nums1),nums2,len(nums2),total/2+1))/2
        else:
            return self.findMedian(nums1,len(nums1),nums2,len(nums2),(total+1)/2)
    '''
    use the dividing algorithm
    '''
    def findMedian(self,list1, m, list2, n, k):
        if m>n:
            return self.findMedian(list2, n, list1, m, k)
        if m == 0:
            return list2[k-1]
        if k ==1:
            return min(list1[0],list2[0])
        pa = min(k/2,m)
        pb = k-pa
        if list1[pa-1]<list2[pb-1]:
            return self.findMedian(list1[pa:],m-pa,list2,n,k-pa)
        elif list1[pa-1]>list2[pb-1]:
            return self.findMedian(list1,m,list2[pb:],n-pb,k-pb)
        else:
            return list1[pa-1]
            
        