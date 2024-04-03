def solution(date1, date2):
    a = int(''.join(map(str, date1)))
    b = int(''.join(map(str, date2)))
    if a < b:
        return 1
    return 0