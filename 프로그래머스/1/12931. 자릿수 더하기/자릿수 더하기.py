def solution(n):
    answer = 0
    temp = list(str(n))
    for i in temp:
        answer+= int(i)
    
    return answer