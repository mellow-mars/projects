k, n = map(int, input().split())
cables = []
for i in range(k):
    cables.append(int(input()))

total = 0

cable_size = max(cables)

while total != n:
    for x in cables:
        total += int(x//cable_size)
    
    if total == n:
        break
    else:
        cable_size -= 1
        total=0
        continue

print(cable_size)
