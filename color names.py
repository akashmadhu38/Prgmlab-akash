n=int(input("Enter a limit:"))
print(f"Enter {n} colour names:")
c=[]
for i in range(0,n):
    c.append(input())
for i in range(0, n):
    print(c[0],c[n-1])
    break
