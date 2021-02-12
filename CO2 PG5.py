n=int(input("Enter a limit:"))
a=0
for i in range(0,n):
    for j in range(0,i+1):
        print(a,end="")
        a += 1
    print("\n")
