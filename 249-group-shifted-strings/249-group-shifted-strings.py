class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
       
        
        mp = defaultdict(list)
        for s in strings:
            key = tuple((ord(c)-ord(s[0]))%26 for c in s)
            print(key)
            mp[key].append(s)
        return mp.values()