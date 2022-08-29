class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        alphabets = list(string.ascii_lowercase)
        
        dict_vectors = defaultdict(list)

        
        for i in range(len(strs)):

            dict_alphabets = { alpha : 0 for alpha in alphabets }
            
            for j in strs[i]:                
                dict_alphabets[j]+=1
            
            
            dict_vectors[strs[i]] .append(dict_alphabets.values())

        dict2 = defaultdict(list)
        
        for k,v in dict_vectors.items():
            
            #print(k,v)
            
            if len(v)>1:
                
                dict2[str(v[0])].extend([k]*len(v))
            else:
                dict2[str(v[0])].append(k)

        return(dict2.values())    
            
            