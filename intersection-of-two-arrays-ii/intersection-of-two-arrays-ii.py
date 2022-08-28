class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        output=[]
        for i in count1:
            if i in count2:
                output.extend([i]*min(count1[i],count2[i]))
        
        return output