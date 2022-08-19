class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        i = 0
        
        while i<len(nums):
            
            #print(i,nums[i],)
            
            if nums[i] == 0 and nums[i:].count(0) != len(nums)-i:
                nums.pop(i)
                #print('nums after pop',nums)
                #print(len(nums)-1-i)
                
                nums.insert(len(nums),0)
                #print('nums after insert',nums)
                #i=i-1
            
            else:
                i=i+1
                
                
        '''       
        for i in range(len(nums)):
            
            print(nums[i])
            
            if nums[i] ==0:
                nums.pop(i)
                print('nums after pop',nums)
                #print(len(nums)-1-i)
                nums.insert(len(nums),0)
                print('nums after insert',nums)
                
                #print(nums)
         '''       
        