class Solution:
    def reverseWords(self, s: str) -> str:
        
        #print(s.split())
        
        return " ".join([i[::-1] for i in s.split()])
