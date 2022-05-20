class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        f=0
        
        while f<len(arr):
            
            if arr[f]==0:
                arr.insert(f,0)
                arr.pop(len(arr)-1)
                
                f = f+2
            
            else:
                f= f+1
            
            