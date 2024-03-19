def solution(a, b):
    
    join = str(a) + str(b)
    multiply = 2*a*b
    
    if int(join) < multiply:
        return multiply
    
    return int(join)