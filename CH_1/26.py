numbers = []

for i in range(10):
    numbers.append(int(input("#{} = ".format(i+1))))

print("Avg = ", sum(numbers) / len(numbers))