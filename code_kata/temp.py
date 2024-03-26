def solution(arr, n):
    answer = []
    length = len(arr)
    if len(arr)&1==0:
        for i in range(len(arr)):
            if i&1==1:
                answer.append(arr(i)+n)
            else:
                answer.append(arr(i))
    else:
        for i in range(len(arr)):
            if i&1==1:
                answer.append(arr(i)+n)
            else:
                answer.append(arr(i))
    return answer

solution([49, 12, 100, 276, 33],27)