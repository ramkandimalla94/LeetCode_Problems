class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hashmap_s ={}
        hashmap_t ={}
        
        if len(s) != len(t):
            return False
        else:
            
            for i in range(len(s)):

                if s[i] in hashmap_s.keys():

                    hashmap_s[s[i]].append(i)
                else:
                    hashmap_s[s[i]] = [i]

            s_values = hashmap_s.values()
            #print(s_values)
            for i in range(len(t)):

                if t[i] in hashmap_t.keys():

                    hashmap_t[t[i]].append(i)
                else:
                    hashmap_t[t[i]] = [i]

            t_values = hashmap_t.values()

            
            print (s_values,t_values)
            
            set_A = {frozenset(i) for i in s_values}
            set_B = {frozenset(i) for i in t_values}

            return set_A == set_B
        

 
