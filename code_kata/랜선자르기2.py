k, n = map(int, input().split())
cables = []
for i in range(k):
    cables.append(int(input()))

min_size = 1
max_size = max(cables)

while min_size <= max_size:
    mid = (min_size+max_size)//2 #기준 숫자를 정해서 계산해보고
    total = 0
    for cable in cables:
        total += cable//mid
    if total>=n: #총 개수가 더 많다면 줄이 더 길어 져야 하기 때문에 왼쪽을 제외
        min_size = mid + 1
    else:  #총 개수가 더 적을 시에는 더 짧아야 하기 때문에 오른쪽을 제외
        max_size = mid - 1
        

print(max_size)
        
