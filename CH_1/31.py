for i in range(2, 1001):
    counter = 0
    for j in range(2, (i//2) + 1):
        if i % j == 0:
            counter += 1
            break
    if counter == 0:
        print(i)