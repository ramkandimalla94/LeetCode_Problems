class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(0,len(nums),2):
                try:
                    
                    if nums[i]!=nums[i+1]:
                        return nums[i]
                except:
                    return nums[-1]
                
                