class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        output = []
        
        end_i = len(matrix)
        end_j = len(matrix[0])
        
        total = end_i * end_j
        
        start_i = 0
        start_j = 0
        
        i, j = 0,0 
        
        while len(output) != total:
            
            if i == start_i and j == start_j:

                for k in range(start_j,end_j):
                    output.append(matrix[start_i][k])

                start_i = start_i + 1
                i = start_i
                j = end_j
                
                continue
                
            if i == start_i and j == end_j:
                
                for k in range(start_i,end_i):
                    output.append(matrix[k][end_j-1])
                    
                end_j = end_j - 1
                i = end_i
                j = end_j
                
                continue
                
            if i == end_i and j == end_j:
                
                for k in reversed(range(start_j,end_j)):
                    output.append(matrix[end_i-1][k])
                
                end_i = end_i -1
                i = end_i
                j = start_j
                
                continue
                
            if i == end_i and j == start_j:
                
                for k in reversed(range(start_i,end_i)):
                    output.append(matrix[k][start_j])
                    
                start_j = start_j + 1     
                i = start_i
                j = start_j
                
                continue
                           
        return output   
            
        
         
            
            
        
            
        