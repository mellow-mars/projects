def solution(order):
    arr = ['3','6','9']
    temp = str(order)
    answer = 0
    for i in temp:
        if i in arr:
            answer += 1
    return answer