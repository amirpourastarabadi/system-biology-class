numbers = []

for i in range(10):
    numbers.append(int(input("#{} = ".format(i+1))))

print("Min = ", min(numbers))