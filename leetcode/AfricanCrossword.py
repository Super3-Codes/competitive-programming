N , M = map(int,input().split())
letters = [] 
output = []

for i in range(N):
    values = (input())
    letters.append(values)

def checker(a, value, col, row):

    colStr = []
    rowStr = []
    for i in range(M):
        if i == col:
            continue
        rowStr.append(letters[row][i])
    rowStr = "".join(rowStr)
   
    if a in rowStr: 
        return False



   
    for j in range(N):
        if j == row:
            continue
        colStr.append(letters[j][col])

    
    colStr = "".join(colStr)
   

    if a in colStr:
        return False
    return True

for i in range(N):
    for j in range(M):
        currValue = letters[i][j]
        if not checker(currValue,letters[i],j,i):
            continue
        else:
            output.append(currValue)

output = "".join(output)
print(output)


    

