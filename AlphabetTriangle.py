num=int(input("Enter number of rows/columns: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    print()