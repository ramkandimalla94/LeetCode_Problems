class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        

        
        #print(A.difference)
        return (list(set(range(1,len(nums)+1)).difference(set(nums))))