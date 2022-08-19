class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        output = float("inf")
        current = 0
        idx = 0
        prevIdx = -1

        while idx < len(nums):
            if prevIdx != idx:
                current += nums[idx]
            prevIdx = idx
            if current >= target:
                output = min(output, idx-l+1)
                current -= nums[l]
                l += 1
            else:
                idx += 1

        if output == float("inf"):
            return 0
        return output
    
        
#         left = 0
#         right = 1
#         min_length = float(inf)
#         i = 0
        
#         if sum(nums) < target:
#             return 0
        
#         while left <= len(nums)-1 and right < len(nums)+1:
#         #while i < 100:  
             
#             print(left,right,min_length) 
#             if sum(nums[left:right]) < target:
#                 right += 1
        
#             else:
#                 min_length = min(min_length,right - left)
                
#                 print(left,right,min_length) 
                  
#                 left += 1
#             #if right == len(nums) +1:
#             #    return min_length
                
#             i +=1
                
#         return min_length         
                
        
        