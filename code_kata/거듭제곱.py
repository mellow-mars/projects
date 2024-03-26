def power(n,m):
    if m==0:
        return 1
    else:
        return  n * power(n, m-1)
    
T = int(input())
test = []

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    print(f"#{test_case} {power(n, m)}")