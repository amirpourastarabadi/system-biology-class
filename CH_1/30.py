numbers = set()
second_maximum = None

for i in range(10):
    numbers.add(int(input("#{} = ".format(i+1))))

numbers = list(numbers)
if len(numbers) > 1:
    second_maximum = numbers[1]
else:
    second_maximum = numbers[0]
     
print("second maximum = ", second_maximum)