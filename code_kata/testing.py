import heapq

T = int(input())

for test_case in range(1, T+1):
    heap = []
    result = []
    n = int(input())
    for i in range(n):
        numbers = list(map(int, input().split()))
        if numbers[0] == 1:
            heapq.heappush(heap, -numbers[1])
        else:
            if heap:
                result.append(-heapq.heappop(heap))
            else:
                result.append(-1)
    print(f"#{test_case} {' '.join(list(map(str, result)))}")
