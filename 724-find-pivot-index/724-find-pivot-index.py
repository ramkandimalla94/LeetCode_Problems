class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum,right_sum=0,0
        right_sum = sum(nums[1:])
        
        #print(left_sum,right_sum)
        
        if left_sum == right_sum:   
            
            return 0
        
        else:
            
            for i in range(1,len(nums)):
                
                left_sum = left_sum + nums[i-1]
                right_sum = right_sum - nums[i]
                
                #print(left_sum,right_sum)

                if left_sum == right_sum:

                    return i               
                    break
                    
                elif i ==len(nums)-1:
                    return -1
            
                
                
                
            
            
            
            
        