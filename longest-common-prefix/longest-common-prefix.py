class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        #print(sorted(strs))
        
        min_length = float(inf)
        for i in strs:
            min_length = min(min_length,len(i))
        
        #print (min_length)
        
        while min_length:
            
            #print (min_length)
            k = [i[:min_length] for i in strs] 
            
            #print (set(k))
            if len(set(k)) == 1:
                break
            else:
                min_length -= 1
            
        return strs[0][:min_length]  
            
            
        
        
        