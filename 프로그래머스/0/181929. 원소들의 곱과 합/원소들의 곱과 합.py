def solution(num_list):
    
    answer1 = (sum(num_list))**2
    answer2 = 1
    
    for i in num_list:
        answer2 *= i
        
    if answer2<answer1:
        return 1
        
    return 0