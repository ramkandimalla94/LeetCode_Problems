class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max_ = float(-inf)
        for i in accounts:
            
            max_ = max(max_,sum(i))
        
        return max_
        