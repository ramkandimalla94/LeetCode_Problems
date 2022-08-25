class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import numpy as np
        
        #nums= np.array(nums)
        #nums_original = nums.copy()
        #nums.sort()
        
        for i in range(len(nums)):
            
            #print(i,target - nums[i])
            
            if target - nums[i] in nums[i+1:] :
                
                return (i,nums[i+1:].index(target-nums[i])+i+1)
                #return (np.where(nums_original==nums[i])[0][0],np.where(nums_original[i+1:]==target - nums[i])[0][0])
                