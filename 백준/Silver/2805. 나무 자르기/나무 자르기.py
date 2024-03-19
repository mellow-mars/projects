n, m = map(int, input().split())
trees = list(map(int,input().split()))

min_size = 1
max_size = max(trees)

while min_size <= max_size:
    mid = (min_size+max_size)//2 #기준 숫자를 정해서 계산해보고
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree-mid
    if total>=m: #총 개수가 더 많다면 줄이 더 많이 필요하기 때문에 짧아져야한다 오른쪽을 소거
        min_size = mid + 1
    else:  #총 개수가 더 많을 시에는 더 길어야 하기 때문에 왼쪽을 소거
        max_size = mid - 1
        

print(max_size)
