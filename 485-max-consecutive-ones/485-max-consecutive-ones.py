class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count=0
       
        k=[]
        for i in range(len(nums)):
            
            if nums[i]==1:
                count+=1
                #print(count)
                
            if nums[i]== 0 or i == len(nums)-1:
                #print(k)
                k.append(count)
                count = 0
                #print(k)
                
        return max(k)    
            
            
        