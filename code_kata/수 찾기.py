n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

for num in m_list:
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if n_list[mid] == num: #숫자가 기준 숫자면 포함됨 1 출력
            print(1)
            break
        elif n_list[mid] > num: #숫자가 기준 숫자보다 작으면 기준 숫자 오른쪽을 소거 
            last = mid - 1
        else: #숫자가 기준숫자보다 크면 왼쪽을 소거
            first = mid + 1
    if n_list[mid] != num: #모든 과정 마치고도 숫자가 일치 하지 않으면 0 출력
        print(0)