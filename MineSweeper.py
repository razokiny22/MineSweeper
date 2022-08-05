
def solution(matrix): 
    li = len(matrix)
    col = len(matrix[0])
    result = []
    T = [-1,0,1]
    for i in range(li):
        temp=[]
        
        for j in range(col):
            
            count=0
            for x in T:
                X = i+x
                for y in T:
                    Y = j+y
                    if not coordoValid(X,Y,li,col):
                        if matrix[X][Y] and (i,j)!=(X,Y):
                            count+=1
            temp.append(count)  
        result.append(temp)
                     
    return result
    
   
def coordoValid(X,Y,li,col):
    return X < 0 or X >= li or Y< 0 or Y>= col 


        
