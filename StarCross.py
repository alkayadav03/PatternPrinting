num=int(input("Enter number of(odd) rows/columns: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        if i == j or i + j == num + 1:
            print(" * ", end=" ")
        else:
            print("   ", end=" ")
    print()