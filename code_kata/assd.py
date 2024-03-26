def solution(age):
    answer = ''
    alpha = 'abcdefghi'
    for i in str(age):
        answer += alpha[int(i)]
    return answer


print(solution(23))
