class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        if numRows > 2:
            
            output = [[1],[1,1]]
            print(output)
            
            for i in range(2,numRows):
                temp_list=[]
                for j in range(i+1):
                    if j == 0 or j == i:    
                        temp_list.append(1)
                    
                    else:
                        temp_list.append(output[i-1][j-1] + output[i-1][j])

                output.append(temp_list)
                
        return output