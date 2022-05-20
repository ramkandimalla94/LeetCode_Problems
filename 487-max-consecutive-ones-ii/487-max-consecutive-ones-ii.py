import numpy as np

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        
        '''
        s=''
        for i in nums:
            s=s+str(i)
        
        list_of_str = s.split('0')
        
        print(list_of_str)
        '''
        
        pos = np.where(np.array(nums) == 0)[0]
        
        
        #print("POS",pos)
        
        if len(pos)==0:
            current_max=len(nums)
        
        
        #sum=0
        
        else:
            
            current_max=len(nums)-pos[-1]

            #print ("POS",pos)
            for i in range(len(pos)):


                if len(pos) ==1:
                    current_max = len(nums)

                else:

                    if i ==0:

                        #print ('1111111')
                        sum = pos[1]

                        #sum = pos[i+1] - pos [i-1] +1

                        if current_max < sum:
                            current_max = sum

                    elif i !=len(pos)-1:

                        #print('222222222')
                        sum = pos[i+1] - pos [i-1] -1

                        if current_max < sum:
                            current_max = sum
                    else:
                        #print('333333333')
                        sum = len(nums) - pos[i-1] -1

                        if current_max < sum:
                            current_max = sum
                
                
            #print(sum,current_max)

        return current_max
        #return len(max(list_of_str,key=len))
            
        