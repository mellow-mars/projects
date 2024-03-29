def solution(s):
    temp = s.lower()
    if temp.count('p') == temp.count('y'):
        return True

    return False