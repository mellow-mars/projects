for test in range(10):

    matrix = []
    count = 0
    n = int(input())
    for _ in range(8):
        matrix.append(input())

    for i in range (8):
        for j in range(8-n+1):
                a = matrix[i][j:j+n]
                if a == a[::-1]:
                    count += 1

    for k in range (8-n+1):
        for l in range(8):
                b = ''
                for m in range(n):
                    b += matrix[k+m][l]
                if b == b[::-1]:
                    count += 1

    print(f"#{test+1} {count}")


