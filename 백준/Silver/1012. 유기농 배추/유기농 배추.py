from collections import deque

def baechoo_bat(m, n, k):

    array = [[0 for _ in range(m)] for _ in range(n)]
    for k in range(k):
        a, b = map(int, input().split())
        array[b][a] = 1
    return array


def bfs(y, x):

    queue = deque([(y, x)])
    field[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            search_y, search_x = y + DY[i], x + DX[i]
            if 0 <= search_x < m and 0 <= search_y < n:
                if field[search_y][search_x] == 1:
                    queue.append((search_y, search_x))
                    field[search_y][search_x] = 0


# 이동할 방향 정의
DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]

T = int(input())

for t in range(T):
    count = 0
    m, n, k = map(int, input().split())
    field = baechoo_bat(m, n, k)

    for y in range(n):
        for x in range(m):
            if field[y][x] == 1:
                count += 1
                bfs(y, x)
                # print(field)

    print(count)
