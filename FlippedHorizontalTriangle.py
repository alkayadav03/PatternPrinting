# num=int(input("Enter number of rows/columns: "))
# for i in range(1,num+1):
#     for j in range(1,num+2-i):   #***** **** *** ** *
#         print(" * ", end=" ")
#     print()



# num=int(input("Enter number of rows/columns: "))
# for i in range(1,num+1):
#     for j in range(num+1-i): # ***** **** *** ** *
#         print(" * ", end=" ")
#     print()




# num=int(input("Enter number of rows/columns: "))
# for i in range(1,num+1):
#     for j in range(1,num+2-i):  # 12345 1234 123 12 1
#         print(j, end=" ")
#     print()




# num=int(input("Enter number of rows/columns: "))
# for i in range(num,0,-1):
#     for j in range(i,0,-1):      #54321 4321 321 21 1
#         print(j, end=" ")
#     print()



# num=int(input("Enter number of rows/columns: "))
# for i in range(1,num+1):
#     for j in range(1,num+2-i):  #abcde abcd abc ab a
#         print(chr(96+j), end=" ")
#     print()


num=int(input("Enter number of rows/columns: "))
for i in range(1,num+1):
    for j in range(1,num+2-i):  #AAAAA BBBB CCC DD E
        print(chr(64+i), end=" ")
    print()


