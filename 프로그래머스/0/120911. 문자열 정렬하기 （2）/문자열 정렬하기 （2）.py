def solution(my_string):
    temp = list(my_string.lower())
    temp.sort()
    return ''.join(temp)
    
    