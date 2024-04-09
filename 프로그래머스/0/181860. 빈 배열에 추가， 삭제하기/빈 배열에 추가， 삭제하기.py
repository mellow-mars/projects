def solution(arr, flag):
    answer = []
    for i, j in zip(flag, arr):
        if i == True:
            answer.extend(list(str(j)*2*j))
        elif i == False:
            answer = answer[:len(answer)-j]
    return list(map(int, answer))