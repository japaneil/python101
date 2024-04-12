matrix = [
    [0,1,1,0],
    [1,0,1,1],
    [0,1,1,1],
    [0,1,0,1]
]

coord = []
x = 0
for i in range(len(matrix)): 
            num = (matrix[i].count(1))
            j = matrix[i].index(1)
            coord.append([i,j])

            if j <= num:
                k = matrix[i].index(1,coord[i][1]+x,len(matrix[i]))
                j = k
                coord.append([i,j])
                # print(coord[i][1])  
            x += 1  
print(coord)
