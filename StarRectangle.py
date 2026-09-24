row=int(input("Enter number of rows: ")) #kitni lines hogi
col=int(input("Enter number of columns: ")) #ek line me kitne stars
for i in range(row):
    for j in range(col):
        print(" * ", end="")
    print()