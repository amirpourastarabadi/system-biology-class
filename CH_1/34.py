n = int(input("Enter a number: "))
counter = 0

for i in range(10, n):
    if n % i == 0:
        counter += 1
        
print("counter =", counter)