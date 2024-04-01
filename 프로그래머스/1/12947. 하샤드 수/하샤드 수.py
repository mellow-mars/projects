def solution(x):
    temp = str(x)
    temp_sum = 0
    for i in temp:
        temp_sum += int(i)
    if x%temp_sum == 0:
        return True
    
    return False