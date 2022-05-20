class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            
            for i in range(n):
                
                nums1.insert(i,nums2[i])
                nums1.pop(n) 
            
        else:    
            
            for j in range(n):
                
                for i in range(m+j-1,-1,-1):

                    if nums2[j] >= nums1[i]:

                        nums1.insert(i+1,nums2[j])
                        nums1.pop(m+1+j)
                        break

                    elif i == 0:

                        nums1.insert(i,nums2[j])
                        nums1.pop(m+1+j)
                        break

                    else:
                        continue
                    
                
                    
                
