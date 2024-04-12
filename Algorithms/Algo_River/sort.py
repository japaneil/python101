matrix = [
    [0,1,1,0],
    [1,0,1,1],
    [0,1,1,1],
    [0,1,0,1]
]

coord = []
x = 0

for i in range(len(matrix)): 
            
            num = 0
            tnum = (matrix[i].count(1))
            j = matrix[i].index(1)
            coord.append([i,j])
            num +=1
            if num < tnum:
                k = matrix[i].index(1,j+x,len(matrix[i]))
                coord.append([i,k])
                num +=1
                if num != tnum:
                    x += 1
                else:
                    x = 0
            
print(coord)
