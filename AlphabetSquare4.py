num=int(input("Enter number of rows/columns: "))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if i % 2 == 0:
            print(chr(i + 64), end=" ")
        else:
            print(chr(i + 96), end=" ")
    print()