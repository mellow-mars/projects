def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        for j, k in parts:
            print(j,k)
            answer += my_strings[i][j:k]
    return answer

solution(["progressive", "hamburger", "hammer", "ahocorasick"],[[0, 4], [1, 2], [3, 5], [7, 7]])