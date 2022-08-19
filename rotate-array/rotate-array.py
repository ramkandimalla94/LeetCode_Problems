class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #print (nums[-k:]+nums[:k])
        
        for i in range(k):
            #print(nums)
            nums.insert(0,nums[-1])
            
            nums.pop()
            #print(nums)