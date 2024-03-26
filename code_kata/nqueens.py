n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(0 for i in range(n)))

def place_queen(a,b):
    matrix[a][b]='Q'
    for i in range(n):
        if matrix[a][i]=='Q':
            pass
        else:
            matrix[a][i]=False
    for j in range(n):
        if matrix[j][b]=='Q':
            pass
        else:
            matrix[j][b]=False


place_queen(3,3)

for i in range(n): 
    print(matrix[i])

