from collections import deque
import sys
input = sys.stdin.readline

T = int(input())


for t in range(T):
    n, m = map(int, input().split())
    que = deque(map(int, input().split()))
    count = 0

    while que:
        m -= 1

        if que[0] == max(que):
            count += 1
            que.popleft()
            if m < 0:
                print(count)
                break
        else:
            que.append(que.popleft())
            if m < 0:
                m = len(que)-1
