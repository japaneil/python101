matrix = [
    [0,1,1,0],
    [1,0,1,1],
    [0,1,1,1],
    [0,1,0,1]
]
tnum = 0
def num(x,y):
    tnum = (matrix[y].count(x))
    return tnum
l_coord = []

for i in range(len(matrix)): 
            x = 1
            cnum = 0
            j = matrix[i].index(1)
            l_coord.append(tuple([i,j]))
            cnum +=1
            while cnum <= num(1,i):
                k = matrix[i].index(1,j+x,len(matrix[i]))
                l_coord.append(tuple([i,k]))
                cnum +=1
                if cnum != num(1,i):
                    x += 1
                    print(cnum == num(1,i))
                    print(x)
                else:
                    x = 0
                    print(cnum == num(1,i))
                    print(x)
s_coord = set(l_coord)    
print(l_coord)        
print(s_coord)