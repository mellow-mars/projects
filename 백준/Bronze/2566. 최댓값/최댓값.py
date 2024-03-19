numbers = []
for i in range(9):
    a = list(map(int, input().split()))
    numbers.append(a)

max_num=0
index_row=0
index_col=0

for row in range(9):
    for column in range(9):
        if numbers[row][column] >= max_num:
            max_num=numbers[row][column]
            index_row = row+1
            index_col = column+1

print(max_num)
print(index_row, index_col)
        

