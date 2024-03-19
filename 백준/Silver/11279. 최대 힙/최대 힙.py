import sys
import heapq
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(numbers, -x)
    elif x == 0:
        if numbers:
            print(heapq.heappop(numbers)*-1)
        else:
            print(0)