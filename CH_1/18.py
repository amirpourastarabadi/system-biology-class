n = int(input("Enter n: "))

counter = 0

for i in range(1, n+1):
    if n % i == 0 and i % 2 == 1:
        counter = counter + 1

print(counter)
