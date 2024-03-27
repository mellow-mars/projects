def solution(num, k):
    answer = str(num)
    k = str(k)
    if k in answer:
        return answer.find(k)+1
    return -1