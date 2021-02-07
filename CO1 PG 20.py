n=int(input("Enter a limit:"))
l=[]
j=[]
print(f"Enter {n} values:")
for i in range(0,n):
    l.append(int(input()))
    if l[i]%2==0:
        j.append(l[i])
print(j)
