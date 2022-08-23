class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print(nums)
        nums.sort()
        #print(nums)
        
        if len(nums) == 1:
            return nums[0]
        else:
#             if len(nums)%2 == 1:
#                 for i in range(1,len(nums),2):

#                     if nums[i]!=nums[i-1]:
#                         return nums[i-1]
#             else:
            for i in range(0,len(nums),2):
                #print(nums[i])
                try:
                    
                    if nums[i]!=nums[i+1]:
                        return nums[i]
                except:
                    return nums[-1]
                
                