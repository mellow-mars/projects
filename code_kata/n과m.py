def recursivenm(n,m,arr=[]):
    if len(arr)==m:
        print(" ".join(map(str,arr)))
        return
    
    for num in range(1, n+1):
        if num not in arr:
            arr.append(num)
            recursivenm(n,m,arr)
            arr.pop()
    
n, m = map(int, input().split())
recursivenm(n,m,arr=[])