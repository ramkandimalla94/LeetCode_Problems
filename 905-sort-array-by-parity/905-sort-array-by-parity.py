class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        #i = 1
        #nums.insert()
        flag=0
        for i in range(len(nums)):
        #while i <len(nums):
            
            if nums[i]%2 ==0:
                
                nums.insert(flag,nums[i])
                nums.pop(i+1)
                #nums.
                flag = flag+1
                
            #else:
                
                #nums.insert(len(nums),nums[i])
                #nums.pop(i)
                
            #print('Nums',nums)
        return nums
            
            #i = i+1
        