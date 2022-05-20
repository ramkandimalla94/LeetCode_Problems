class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        check_climb = True
        
        for i in range(1,len(arr)):
            
            if len(arr) > 2:
                
                if check_climb:
                    
                    if arr[i] > arr[i-1]:
                        continue
                    elif arr[i] == arr[i-1]:
                        break
                    elif i==1 and arr[i] < arr[i-1]:
                        break
                    else:
                        check_climb = False
                else:

                    if arr[i] >= arr[i-1]:
                        break

                if i == len(arr)-1:
                    return True
                
            else:
                break

        
        
                
                
                
        