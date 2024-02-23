numbers = set()
second_minimum = None

for i in range(10):
    numbers.add(int(input("#{} = ".format(i+1))))

numbers = list(numbers)
if len(numbers) > 1:
    second_minimum = numbers[1]
else:
    second_minimum = numbers[0]
     
print("second minimum = ", second_minimum)