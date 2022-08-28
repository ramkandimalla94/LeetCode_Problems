class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        my_dict = {}
        
        for i in range(len(nums)):
            
            try:
                
                my_dict[nums[i]].append(i)
            except:
                my_dict[nums[i]] = [i]
        #print(my_dict)    
        
        for values in my_dict.values():
            
            for i in range(len(values)-1):
                if abs(values[i]-values[i+1]) <=k:
                    return True
#             if len(values)>1:
#                 l_iter = iter(values) 
                
      
#                 while True:
#                     try:
#                         initial = next(l_iter)
#                         print(initial)
#                         if (abs(initial - next(l_iter))<=k):
                            
#                             return True
#                     except:
#                         return False
#                     #initial = next(values)        