class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #return len(nums) != len(set(nums))
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set.add(i)
            
           
        