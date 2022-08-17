class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        sum_ = sum (nums[::2])
       
        return sum_