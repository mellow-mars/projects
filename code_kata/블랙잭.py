N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = []
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            res.append(cards[i]+cards[j]+cards[k])

res.sort()

ans = 0
for l in res:
    if l <= M:
        ans = l

print(ans)
