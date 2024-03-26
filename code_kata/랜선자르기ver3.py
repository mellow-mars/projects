k, n = map(int, input().split())
cables = []
for i in range(k):
    cables.append(int(input()))

left = 1
right = max(cables)
answer = 0  # 정답

while left <= right:
    mid = (left + right) // 2  # updown ?

    total = 0
    for cable in cables:
        total += cable // mid

    if total >= n:
        answer = mid  # 케이블 개수가 목표치 이상이라면 정답을 업데이트하고
        left = mid + 1  # 더 큰 mid를 탐색
    else:
        right = mid - 1  # 케이블 개수가 목표치보다 작다면 더 작은 mid를 탐색

print(answer)