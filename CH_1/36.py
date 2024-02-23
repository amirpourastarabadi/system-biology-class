# this is a function defnition
# we will talk about if
# now just understand the code inside of is_prime
def is_prime(n):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    
    return True




primes = []
for i in range(3):
    n = int(input("Enter a number: "))
    if is_prime(n):
        primes.append(n)

print(primes)


