import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test in range(1, T + 1):

    total = 0

    matrix = []
    n, k = map(int, input().split())

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n-k+1):
            if sum(matrix[i][j:j+k]) == k:
                if j != 0 and matrix[i][j-1] == 1:
                    continue
                elif j+k != n and matrix[i][j+k] == 1:
                    continue
                else:
                    total += 1

    for x in range(n):
        for y in range(n-k+1):
            nums = []
            for z in range(k):
                nums.append(matrix[y+z][x])
            if sum(nums) == k:
                try:
                    if matrix[y+k+1][x] == 0 or matrix[y-1][x] == 0 or (matrix[y+k+1][x] == 0 and matrix[y-1][x] == 0):
                        total += 1
                except:
                    total += 1

    print(f"#{test} {total}")
