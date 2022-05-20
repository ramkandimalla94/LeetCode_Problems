class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digit_map = map(str,digits)
        
        number = ''.join(digit_map)
        
        return map(int,list(str(int(number)+1)))

        
        