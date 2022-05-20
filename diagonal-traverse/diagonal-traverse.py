class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        #print(mat)
        output=[]
        m = len(mat)
        n = len(mat[0])
        
        i,j=0,0
        output.append(mat[i][j])
        
        direction = 1 
        
        while i < m and j< n:
            
            
            #print (i,j)
            
            if i == m-1 and j ==n-1:
                #output.append(mat[i][j])
                #print (output)
                break
            
            if direction:

                if i == 0 and j != n-1:
                    
                    #print ('1')
                    j = j+1
                    output.append(mat[i][j])
                    direction = 0
                    
                elif j == n-1:   
                    #print ('2')
                    i = i+1
                    output.append(mat[i][j])
                    direction = 0
    
                else:
                    #print ('3')
                    i = i-1
                    j = j+1
                    output.append(mat[i][j])
            else:
                
                if j == 0 and i!=m-1:
                    #print ('4')
                    i =i+1
                    output.append(mat[i][j])
                    direction = 1
                    
                elif i == m-1:  
                    #print ('5')
                    j  = j+1
                    output.append(mat[i][j])
                    direction = 1
                    
                else:
                    #print ('6')
                    j = j-1
                    i=i+1
                    output.append(mat[i][j])
                    
            
            #print (output)      
        return output
            
                    
                
                
        