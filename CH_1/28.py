numbers = []

for i in range(10):
    numbers.append(int(input("#{} = ".format(i+1))))

maximum = numbers[0]
for i in numbers[1:]:
    if i > maximum:
        maximum = i


print("Max = ", maximum)