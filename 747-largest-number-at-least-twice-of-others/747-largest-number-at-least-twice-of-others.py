class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        '''
        sorted_nums=sorted(nums)
        #print(nums,sorted_nums)
        
        if len(nums) == 1:
            return 0
        elif sorted_nums[-1] >= 2*sorted_nums[-2]:
            return nums.index(sorted_nums[-1])
        else:
            return -1
        
        '''
        
        if len(nums) == 1:
            return 0
        
        #elif  True:
        max_num = max(nums)
        #print(max_num)
        _index = nums.index(max_num)
        nums.remove(max_num)
        #print(nums)
        max_num_2=max(nums)
        
        if max_num >= 2*max_num_2:
            return _index
        else:
            return -1
            
           