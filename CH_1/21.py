n = int(input("Enter n: "))

counter = 0
total = 0

for i in range(1, n+1):
    if n % i == 0:
        counter = counter + 1
        total = total + i

avg = total / counter
print("avg = ", avg)
