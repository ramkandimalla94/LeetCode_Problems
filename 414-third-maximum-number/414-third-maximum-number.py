class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        nums.sort(reverse=True)
        sorted_distinct_elements = list(dict.fromkeys(nums))
        
        #print(sorted_distinct_elements)
        
        if len(sorted_distinct_elements) ==1:
            return sorted_distinct_elements[0]
        
        elif len(sorted_distinct_elements) ==2:
            return sorted_distinct_elements[0]
        
        else:
            return list(dict.fromkeys(nums))[2]

            
            
        