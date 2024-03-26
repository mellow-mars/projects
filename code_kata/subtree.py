import sys
sys.stdin = open("input.txt", "r")


def preorder(n):
    global result
    if n:
        result += 1
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())

for test_case in range(1, T+1):
    E, N = map(int, input().split())
    inputlist = list(map(int, input().split()))

    result = 0
    #노드의 개수는 E+1 이고 나는 0번째 리스트 요소를 안쓸꺼니까, +1을 더해서
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)

    for i in range(0, len(inputlist),2):
        parent, child = inputlist[i], inputlist[i+1]

        if ch1[parent] == 0:
            ch1[parent] = child
        else:
            ch2[parent] = child
    preorder(N)
    print(f"#{test_case} {result}")
