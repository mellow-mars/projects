n = int(input())

for i in range(1, n+1):
    num = sum(map(int, str(i)))
    num_total = num + i

    if num_total == n:
        print(i)
        break
    if i == n:
        print(0)
