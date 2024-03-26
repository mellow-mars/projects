def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


prime_array = prime_list(10000)
print(prime_array)
T = int(input())

for i in range(T):
    n = int(input())
    half_n = int(n/2)
    for i in range(len(prime_array)):
        for j in range(len(prime_array)):
            if prime_array[i] + prime_array[j] == n and prime_array[i] < prime_array[j]:
                print(prime_array[i], prime_array[j])
