class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        output =[]
        if rowIndex == 0:
            output.append([1])
        if rowIndex == 1:
            output.append([1])
            output.append([1,1])

        if rowIndex >= 2:
            
            output = [[1],[1,1]]
            #print(output)
            
            for i in range(2,rowIndex+1):
                temp_list=[]
                for j in range(i+1):
                    if j == 0 or j == i:    
                        temp_list.append(1)
                    
                    else:
                        temp_list.append(output[i-1][j-1] + output[i-1][j])

                output.append(temp_list)
        print (output)        
        return output[rowIndex]