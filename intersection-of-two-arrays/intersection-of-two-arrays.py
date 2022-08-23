class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #print (nums1-nums2)
        #print (nums1+nums2)
        l = [nums1,nums2]
        if len(nums1) > len(nums2):
            
            temp_dictionary = dict.fromkeys(nums1, True)
            flag = 1
        else:
            temp_dictionary = dict.fromkeys(nums2, True)
            flag = 0
        
        set_ = set()
        for i in l[flag]:
            
            if i in temp_dictionary:
                set_.add(i)
        return set_        
            