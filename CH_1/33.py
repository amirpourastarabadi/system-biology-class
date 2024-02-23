n = int(input("Enter a number: "))
total = 0

for i in range(10, n):
    if n % i == 0:
        total += i
        
print("total =", total)