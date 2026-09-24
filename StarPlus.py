num=int(input("Enter number of(odd) rows/columns: "))
mid=num//2+1
for i in range(1,num+1):
    for j in range(1,num+1):
        if(i==mid or j==mid):
            print(" * ", end="")
        else:
            print("   ", end="")
    print()