x = ''

while len(x) < 5:
    y = input("Enter anything: ")
    if y == 'o':
        continue
    if y == "quit":
        break

    x += y
else:
    print(x)

print("Program is working...")
