m = 123456*2
primes = list(1 for i in range(m+1))
primes[0]= 0
primes[1]= 0
for i in range(int(m)+1):
    if primes[i]:
        for j in range(2*i, int(m)+1, i):
            primes[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(sum(primes[n+1:2*n+1]))