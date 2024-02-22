# vertion 1
total = 0
for num in range(1, 101):
    if num % 2 == 1:
        total = total + num 

print("V1 :", total)

# vertion 2
total = 0
for num in range(1, 101, 2): # in each iteration num = last num + 2
    total = total + num 

print("V2 :", total)