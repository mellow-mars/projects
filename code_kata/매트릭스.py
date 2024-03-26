map_array = [[0]*100 for _ in range(100)]

n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    
    for j in range(y,y+10):
        id_y = j
        for k in range(x,x+10):
            id_x = k
            if map_array[id_y][id_x]==0:
                map_array[id_y][id_x]=1
            else:
                pass

area = 0

for i in range(100):
    area+=sum(map_array[i])

print(area)

