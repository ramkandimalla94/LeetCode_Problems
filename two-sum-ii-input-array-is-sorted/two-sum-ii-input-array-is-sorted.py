class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #2 pointers Method, initialize pointers
        #We will use pointers to access List index 
        
        left = 0
        right = len(numbers) - 1
        
        while (left < right):                           #Loop both pointers till midpoint ONLY
            
            if numbers[left] + numbers[right] == target:
                return (left+1, right+1)                     #sum found, return the indices
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
                
            else:   left += 1
                
                
                
                
                
                
                
           

        