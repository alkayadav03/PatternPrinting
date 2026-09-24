# num=int(input("Enter number of rows/columns: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(2*j - 1, end=" ")
#     print()


num=int(input("Enter number of rows/columns: "))
a=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(a, end=" ")
        a += 2
    print()
