#pattern using loop
n=int(input("Enter number of rows in pattern :"))
i=1
while i<n+1:
    for c in range(1,i+1):
        print(c,end=" ")
    print()
    i+=1