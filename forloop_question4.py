# pattern using loop
n=int(input("Enter the number of rows in pattern: "))
i=n
while i>0:
    for c in range(1,i+1):
        print(c,end=" ")
    print()
    i-=1