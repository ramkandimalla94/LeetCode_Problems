class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            
            if i != len(arr) -1:   
                
                arr.insert(i,max(arr[i+1:]))
                arr.pop(i+1)       
                
            else:          
                
                arr.insert(i,-1)
                arr.pop(i+1)
                
        return arr      
    