def solution(n):
    temp = reversed(str(n))
    answer = []
    for i in temp:
        answer.append(int(i))
    
    return answer