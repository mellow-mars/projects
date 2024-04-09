def solution(my_string, indices):
    temp = list(my_string)
    a = indices
    a.sort(reverse = True)
    for i in a:
        del temp[i]        
    return ''.join(temp)