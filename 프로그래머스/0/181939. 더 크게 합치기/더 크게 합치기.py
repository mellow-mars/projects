def solution(a, b):
    
    ab=str(a)+str(b)
    ba=str(b)+str(a)
    
    if int(ba) > int(ab):
        return int(ba)
        
    return int(ab)