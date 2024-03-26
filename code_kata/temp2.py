def solution(myString, pat):
    
    dict = {'A':'B' , 'B':'A'}
    
    word = ''

    for i in myString:
        word+=dict[i]    
    
    if pat in word:
        return 1
    
    return 0

solution("ABBAA", "AABB")