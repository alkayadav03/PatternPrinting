num=int(input("Enter number of rows/columns: "))
a=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(a, end=" ")
        a += 1
    print()