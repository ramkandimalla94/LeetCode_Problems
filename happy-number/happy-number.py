class Solution(object):
    
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        import numpy as np
        i = 0
        while n!=1:
            print(np.square(list(map(int, list(str(n))))))
            n = (np.sum(np.square(list(map(int, list(str(n)))))))
            print(n)
            if n < 10 and n!=1 and n!=7:
                return False
        return True