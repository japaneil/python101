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
            add = j
            cnum +=1
            while cnum <= num(1,i):
                if add > len(matrix[i]):
                    add = add - (add - len(matrix[i]))
                k = matrix[i].index(1,j+x)
                l_coord.append(tuple([i,k]))
                add = k
                cnum +=1
                print(add+x)
                if cnum != num(1,i):
                    x += 1
                    print(cnum == num(1,i))
                    # print(x)
                else:
                    x = 0
                    print(cnum == num(1,i))
                    
                    # print(k)
s_coord = set(l_coord)    
print(l_coord)        
print(s_coord)