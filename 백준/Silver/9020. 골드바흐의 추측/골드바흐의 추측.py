m = 10000
numb = list(i for i in range(m+1))
numb[0] = 0
numb[1] = 0
for i in range(int(m)+1):
    if numb[i]:
        for j in range(2*i, int(m)+1, i):
            numb[j] = 0

prime = [i for i in numb if i != 0]

T = int(input())

for test in range(T):
    n = int(input())
    half = n/2
    for i in range(len(prime)):
        if half-i in prime and half+i in prime:
            print(int(half-i), int(half+i))
            break

