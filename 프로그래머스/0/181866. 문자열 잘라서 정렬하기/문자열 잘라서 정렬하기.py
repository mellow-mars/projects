def solution(myString):
    answer = []
    for i in list(map(str, myString.split('x'))):
        if i:
            answer.append(i)
        answer.sort()
    return answer