def solution(my_string, m, c):
    temp = []
    answer = ''
    for i in range(0,len(my_string),m):
        temp.append(my_string[i:i+m])
    for i in temp:
        answer += i[c-1]
    return answer