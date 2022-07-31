while True:
    x = int(input("Enter any value: "))
    count = 0
    y = 1

    while count < x:
        count += 1
        y *= count
    else:
        print(y)
