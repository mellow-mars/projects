def solution(n):
    answer = 0
    
    if n&1 == 0:
        for i in range(n+1):
            if i&1==0:
                answer+=i**2
    else:
        for i in range(n+1):
            if i&1==1:
                answer+=i
    return answer