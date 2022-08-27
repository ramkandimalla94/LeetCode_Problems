class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        
        for i in range(len(s)):
            
            if s[i] in d:
                d[s[i]] = len(s)
                #d[s[i]].append(i)
            else:
                d[s[i]] = i
        
        #print(d)
        temp = min(d.values())
        
        if temp == len(s):
            return -1
        else:
            
            res = [key for key in d if d[key] == temp]
            #print(res)
            return (d[res[0]])        