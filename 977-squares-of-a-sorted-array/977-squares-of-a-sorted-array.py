class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squares = [ i*i for i in nums ] 

        return sorted(squares)