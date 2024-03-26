def solution(n):
    answer = []
    while n != 1:
        if n%2 == 0:
            n = n/2
            answer.append(n)
        else:
            n = 3*n+1
            answer.append(n)
    return answer

print(solution(10))