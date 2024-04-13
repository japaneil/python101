matrix = [
    [0,1,1,0],
    [1,0,1,1],
    [0,1,1,1],
    [0,1,0,1]
]
tnum = 0
def num(x: int):
    tnum = (matrix[i].count(x))
    return tnum
l_coord = []
x = 1

for i in range(len(matrix)): 
            cnum = 0
            j = matrix[i].index(1)
            l_coord.append(tuple([i,j]))
            cnum +=1
            while cnum <= num(1):
                k = matrix[i].index(1,j+x,len(matrix[i]))
                l_coord.append(tuple([i,k]))
                cnum +=1
                if cnum != num(1):
                    x += 1
                    print(cnum == num(1))
                    print(x)
                else:
                    x = 0
                    print(cnum == num(1))
s_coord = set(l_coord)    
print(l_coord)        
print(s_coord)