n = int(input("Enter n: "))

counter = 0

for i in range(2, (n//2) + 1):
    if n % i == 0:
        counter += 1
        break;

print("Yes" if counter == 0 else "No")