n = int(input("Enter n: "))
m = int(input("Enter m: "))

n_primes = []
m_primes = []

# find unit primes of n
i = 2
while n > 0 and i <= n:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        while n % i == 0:
            n = n // i
            n_primes.append(i)
    i = i + 1

# find unit primes of m
i = 2
while m > 0 and i <= m:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        while m % i == 0:
            m = m // i
            m_primes.append(i)
    i = i + 1

# copyt n,m_primes to a new list to keep original list safe from changes
temp_n_prime = n_primes.copy() 
temp_m_prime = m_primes.copy()

intercept_primes = []
for i in temp_n_prime:
    if i in temp_m_prime:
        intercept_primes.append(i)
        temp_m_prime.remove(i)

BMM = 1
for i in intercept_primes:
    BMM *= i
print("BMM = ", BMM)

    
intercept_primes = []
for i in n_primes:
    intercept_primes.append(i)
    if i in m_primes:
        m_primes.remove(i)
intercept_primes.extend(m_primes)


KMM = 1
for i in intercept_primes:
    KMM *= i
print("KMM = ", KMM)
