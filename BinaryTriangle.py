# num=int(input("Enter number of rows/columns: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         if i==j or (i+j) %2==0:
#             print(" 1 ", end=" ")
#         elif (i+j) %2!=0:
#             print(" 0 ", end=" ")
#         else:
#             print("   ", end=" ")
#     print()



num=int(input("Enter number of rows/columns: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if (i+j) %2==0:
            print(" 1 ", end=" ")
        elif (i+j) %2!=0:
            print(" 0 ", end=" ")
        else:
            print("   ", end=" ")
    print()