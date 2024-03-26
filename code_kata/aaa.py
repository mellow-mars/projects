m = 10000
numb = list(i for i in range(m+1) if i)
numb[0] = 0
numb[1] = 0
for i in range(int(m)+1):
    if numb[i]:
        for j in range(2*i, int(m)+1, i):
            numb[j] = 0

prime = [i for i in numb if i != 0]

# T = int(input())

# for test in range(T):
#     n = int(input())
#     combs = []
#     for i in range(len(prime)):
#         for j in range(len(prime)):
#             if prime[i] < prime[j] and prime[i] + prime[j] == n:
#                 combs.append([prime[i],prime[j],prime[j]-prime[i]])

#     combs.sort(key = lambda x: x[2])
    
#     print(combs[0][0], combs[0][1])

T = int(input())

for test in range(T):
    n = int(input())
    half = n/2
    for i in range(int(half)//2):
        if half-i in prime and half+i in prime:
            print(int(half-i), int(half+i))
            break


