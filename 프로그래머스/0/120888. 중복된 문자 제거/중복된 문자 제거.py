def solution(my_string):
    answer = ''
    unique_letters = set(my_string)
    for i in my_string:
        if i in unique_letters:
            answer += i
            unique_letters.discard(i)
    return answer